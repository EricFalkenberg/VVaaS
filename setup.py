#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="deploy_vvaas",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points = {
        'console_scripts' : [
            'deploy_vvaas = src.deploy_vvaas:cli'
        ]
    }
)  

setup(name="install_vvaas",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points = {
        'console_scripts' : [
            'install_vvaas = src.install_vvaas:cli'
        ]
    }
)  
