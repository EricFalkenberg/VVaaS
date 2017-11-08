# VVaaS
Vegan Volcanoes as a Service

### Installation
This project is meant to be run on a Raspberry Pi host. As such, you'll need to download the tool suite for interacting with such hosts. You'll also want to install the tools contained in this repo.
```
virtualenv venv
source venv/bin/activate
pip install git+https://github.com/EricFalkenberg/raspi_tools
pip install git+https://github.com/EricFalkenberg/VVaaS
```
Flash your SD with `flash_sd`
```
Usage: flash_sd [OPTIONS] RASPBIAN_IMAGE

  Flash a rasbian image onto your SD card.

Options:
  --help  Show this message and exit.
```
Once your SD is flashed, you can plug it into your raspberry pi and hook it up to the network and find int on the LAN with `discover_rpi`
```
Usage: discover_rpi [OPTIONS] [SUBNET]

  Discover Raspberry Pi hosts on local network and deploy to them. Must be
  run as root user.

Options:
  --help  Show this message and exit.
```
The subnet argument defaults to `192.168.0.0/24` so if yours is different you'll have to specify.

### Deployment
Find the IP of the host you want to install to and use it with `deploy_vvaas`.
```
Usage: deploy_vvaas [OPTIONS] IP

  Deploy VVaaS to the specified Raspberry Pi host

Options:
  --help  Show this message and exit.
```
