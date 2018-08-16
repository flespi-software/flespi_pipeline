Flespi Pipeline
===============

This library is used to get messages from flespi gateway channel via MQTT connection, process it according to Private Data Switch algorithm and publish to specified topic.

Getting started:
This library is written using `gmqtt <https://github.com/wialon/gmqtt>`_ library for Python 3.5 version. To run the example script do:

1. **make init**:
initialize local virtual environment with python3.5 and set up all required libraries

2. edit **pipeline.py**:
write your parameters in ``# configure pipeline`` section

3. **make test**:
runs pipeline.py script

More info in `flespi blog <https://flespi.com/blog/private-data-switch-gdpr-compliance-and-personal-location-data-protection>`_

