# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='flespi_pipeline',
    version='0.1.0',
    description='MQTT pipeline for telemetry messages from flespi.io',
    long_description=readme,
    author='Jan Bartnitsky',
    author_email='baja@gurtam.com',
    url='https://github.com/flespi-software/flespi_pipeline',
    license=license,
    packages=find_packages(exclude=('docs'))
)

