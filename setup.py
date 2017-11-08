#!/usr/bin/env python

from setuptools import setup

setup(name="deploy",
    version="0.0.1",
    modules=["deploy"],
    install_requires=[
        'click'
    ],
    entry_points = {
        'console_scripts' : [
            'deploy = src.deploy:cli'
        ]
    }
)  
