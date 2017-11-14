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
Create a file of the following format called `twilio.cfg`.
```
[account]
sid: <twilio_sid_here>
auth: <twilio_auth_id_here>
```
Fill in account information using your own Twilio account.

Finally, use `deploy_vvaas` to deploy the project.
```
Usage: deploy_vvaas [OPTIONS] FROM_NUMBER TO_NUMBER TWILIO_CFG IP

  Deploy VVaaS to the specified Raspberry Pi host

Options:
  --help  Show this message and exit.
```
```
deploy_vvaas <TWILIO_NUMBER> <TARGET_NUMBER> <TWILIO_CFG_PATH> `sudo discover_rpi [SUBNET]`
```
