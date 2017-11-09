# VVaaS
Vegan Volcano as a Service

### Installation
This project is meant to be run on a Raspberry Pi so you'll need to install the tool suite for interacting with such hosts. You'll also want to install the tools contained in this repo.
```
virtualenv venv
source venv/bin/activate
pip install git+https://github.com/EricFalkenberg/raspi_tools
pip install git+https://github.com/EricFalkenberg/VVaaS
```

### Deployment
Find the IP of the host you want to install to and pass it to `deploy_vvaas`. The `raspi_tools` suite has a binary for doing this automatically assuming a Raspberry Pi is connected to the network.
```
Usage: deploy_vvaas [OPTIONS] IP

  Deploy VVaaS to the specified Raspberry Pi host

Options:
  --help  Show this message and exit.
```
```
deploy_vvaas <TWILIO_NUMBER> <TARGET_NUMBER> `sudo discover_rpi [SUBNET]`
```
