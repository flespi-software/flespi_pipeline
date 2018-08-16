Flespi Pipeline Autostart Facility
==================================

To make flespi_pipeline running as a system service and start automatically when your OS is starting up you need to perform this steps:

1. Detect your OS init system
-----------------------------

1.1. **System V** is the older init system:

* Debian 6 and earlier
* Ubuntu 9.04 and earlier
* CentOS 5 and earlier

1.2 **Upstart**:

* Ubuntu 9.10 to Ubuntu 14.10, including Ubuntu 14.04
* CentOS 6

1.3 **systemd** is the init system for the most recent distributions featured here:

* Debian 7 and Debian 8
* Ubuntu 15.04 and newer
* CentOS 7

2. Install service according your OS init system
------------------------------------------------

2.1 **System V**:

2.2 **Upstart**:

* Configure **flespi_pipeline** project to run in foreground (see main README.rst file)
* Change ``export ROOT="/path/to/flespi_pipeline"`` in file ``autostart/upstart/flespi_pipeline.conf`` according your installation
* Copy service file ``autostart/upstart/flespi_pipeline.conf`` to ``/etc/init/flespi_pipeline.conf``
* Execute ``chown root:root /etc/init/flespi_pipeline.conf``
* Execute ``chmod 0644 /etc/init/flespi_pipeline.conf``
* Start the service with command ``service flespi_pipeline start``

2.3 **systemd**:
