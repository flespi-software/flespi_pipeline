# configure merging pipeline
ch_id = 1                                       # channel to subscribe
publish_topic = 'custom/topic/injected'         # custom topic to publish messages with injected parameters
username = 'FlespiToken '                       # token with ACL to channel above and to publish_topic
mqtt_client_id = 'flespi_injecting_pipeline_%s' % ch_id   # client id to use for MQTT session
broker_host = 'mqtt.flespi.io'                  # MQTT broker host
qos = 1                                         # MQTT qos to publish/subscribe

# import requirements
import asyncio
import signal
import json
import uvloop

from gmqtt import Client as MQTTClient

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
STOP = asyncio.Event()

# on message received: process message according to Private data switch logic
# publish processed message to specified topic
def on_message(client, topic, payload, qos, properties):
    try:
        message_json = json.loads(payload.decode("utf-8"))
    except ValueError:
        print('invalid JSON received: ' + payload.decode("utf-8"))
        return

    # perform message injection here: e.g. add parameter 'injection' with value 'test'
    message_json['injection'] = 'test'

    # dump payload and publish it back to broker
    payload = json.dumps([message_json])
    client.publish(publish_topic, payload)

# below is example from gmqtt python library README
# https://github.com/wialon/gmqtt
def on_connect(client, flags, rc, properties):
    subscr_topic = 'flespi/message/gw/channels/' + str(ch_id) + '/+'
    print('Connected. Trying to subscribe to ' + subscr_topic)
    client.subscribe(subscr_topic, qos)

def on_disconnect(client, packet, exc=None):
    print('Disconnected')

def on_subscribe(client, mid, qos, properties):
    print('Subscribed')

def ask_exit(*args):
    STOP.set()

async def main():
    client = MQTTClient(mqtt_client_id, session_expiry_interval=86400*10, clean_session=False)

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
