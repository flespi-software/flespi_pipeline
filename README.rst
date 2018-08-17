Flespi Pipeline
===============

This library is used to get messages from flespi gateway channel via MQTT connection, process it according to Private Data Switch algorithm and publish to specified topic.

Getting started:
This library is written using `gmqtt <https://github.com/wialon/gmqtt>`_ library for Python 3.5 version. To run the example script do:


Requirements
------------

**System requirements:**

* Python version 3.5 or higher
* `GNU make <https://www.gnu.org/software/make/>`_
* `virtualenv <https://github.com/pypa/virtualenv>`_

Note: please install this requirements according your OS.

**Python requirements:**

* `gmqtt <https://github.com/wialon/gmqtt>`_

Note: this will be automatically installed in the section below.

How to start
------------

1. **make init**:
initialize local virtual environment with python3.5 and set up all required python libraries

2. edit **pipeline.py**:
write your parameters in ``# configure pipeline`` section

3. **make run**:
runs pipeline.py script

More info in `flespi blog <https://flespi.com/blog/private-data-switch-gdpr-compliance-and-personal-location-data-protection>`_


Autostart and running as a system service (daemon)
--------------------------------------------------

To make this script runs as a daemon on system start - see README.rst in `autostart folder <https://github.com/flespi-software/flespi_pipeline/tree/master/autostart>`_
