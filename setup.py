#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="vvaas",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'twilio',
        'configparser',
        'paramiko',
        'scp'
    ],
    entry_points = {
        'console_scripts' : [
            'deploy_vvaas = src.deploy_vvaas:cli',
            'order_vv = src.order_vv:cli'
        ]
    }
)  
