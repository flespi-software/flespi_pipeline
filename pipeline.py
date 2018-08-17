import asyncio
import signal
import json
import uvloop

from gmqtt import Client as MQTTClient

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
STOP = asyncio.Event()

# pds_check_type function to simply test parameter value equals to configured
def check_value(value):
    global pds_turn_on_value
    return value == pds_turn_on_value

# pds_check_type function to test configured bit is set
def check_bit_set(value):
    global pds_turn_on_value
    return((value >> (pds_turn_on_value - 1)) & 0x1) != 0

# pds_check_type function to test configured bit is NOT set
def check_bit_not_set(value):
    global pds_turn_on_value
    return((value >> (pds_turn_on_value - 1)) & 0x1) == 0

# configure pipeline
ch_id = 1                                       # channel to subscribe
username = 'FlespiToken '                       # token with ACL to channel above
mqtt_client_id = 'flespi_pipeline_%s' % ch_id   # client id to use for MQTT session
broker_host = 'mqtt.flespi.io'                  # MQTT broker host
publish_topic = 'custom/topic/pds'              # custom topic for private data switch
qos = 1                                         # MQTT qos to publish/subscribe
pds_check_type = check_bit_set                  # private data switch check type: check_value, check_bit_set or check_bit_not_set function
pds_parameter_name = 'custom.din_index'         # private data switch parameter name
pds_turn_on_value = 1                           # private data switch turn on value or bit number

# on message received: process message according to Private data switch logic
# publish processed message to specified topic
def on_message(client, topic, payload, qos, properties):
    try:
        message_json = json.loads(payload.decode("utf-8"))
    except ValueError:
        print('invalid JSON received: ' + payload.decode("utf-8"))
        return

    # define if pipline message processing required
    if pds_parameter_name in message_json and pds_check_type(message_json[pds_parameter_name]):
        processed_msg = {}
        # iterate over message parameters and exclude position info
        for parameter in message_json:
            # if parameter starts from "position" or "gsm" - exclude it from message
            if not (parameter.startswith('position') or parameter.startswith('gsm')):
                processed_msg[parameter] = message_json[parameter]
        payload = json.dumps(processed_msg)

    # publish processed(or not) message
    client.publish(publish_topic, payload)

# below is example from gmqtt python library README
# https://github.com/wialon/gmqtt
def on_connect(client, flags, rc, properties):
    subscr_topic = 'flespi/message/gw/channels/' + str(ch_id) + '/+'
    print('Connected. Trying to subscribe to ' + subscr_topic)
    client.subscribe(subscr_topic, qos)

def on_disconnect(client, packet, exc=None):
    print('Disconnected')

def on_subscribe(client, mid, qos):
    print('Subscribed')

def ask_exit(*args):
    STOP.set()

async def main():
    client = MQTTClient(mqtt_client_id)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    client.set_auth_credentials(username, None)
    await client.connect(broker_host)
    await STOP.wait()
    await client.disconnect()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, ask_exit)
    loop.add_signal_handler(signal.SIGTERM, ask_exit)

    loop.run_until_complete(main())