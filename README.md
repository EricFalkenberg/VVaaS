# Vegan Volcano as a Service (VVaaS&trade;)
As society moves further toward a mobile-first, cloud-focused environment, it just makes sense for vegans to follow suit, keeping everything on the cloud where it is accessible and up-to-date 24/7.

Face it: this is America. We like to level the playing field for the under-dog and allow the American dream to come true. VVaaS&trade; allows for the “democratization of vegan volcanoes” in almost every possible way. For as a society that moves fast and likes to keep its options open for the next big thing, VVaaS&trade; is the perfect solution.

Call the Rainforest Cafe every day using bleeding edge Cron-Technology&trade;&reg;&copy; and order five (5) vegan volcanoes.

### Installation
This project is meant to be run on a Raspberry Pi so you'll need to install the tool suite for interacting with such hosts. You'll also want to install the tools contained in this repo.
```
virtualenv venv
source venv/bin/activate
pip install git+https://github.com/EricFalkenberg/raspi_tools
pip install git+https://github.com/EricFalkenberg/VVaaS
```
[More information about the raspi_tools suite can be found here.](https://github.com/EricFalkenberg/raspi_tools/blob/master/README.md)

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
