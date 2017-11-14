#!/usr/bin/python
import click
import subprocess
import getpass
import paramiko
from scp import SCPClient

DEPENDENCIES = [
    'python-pip', 'python-dev', 'git', 
    'libffi-dev', 'libssl-dev', 'libxml2-dev', 
    'libxslt1-dev', 'libjpeg8-dev', 'zlib1g-dev'
    ]
RPI_USERNAME = 'pi'
DEFAULT_SSH_PORT = 22
APT_UPDATE  = 'sudo apt-get update --fix-missing'
APT_INSTALL = 'sudo apt-get -y install {0}'.format(' '.join(DEPENDENCIES)) 
VENV_INSTALL = 'sudo pip install virtualenv'
RM_OLD_VENV = 'rm -r venv'
RM_OLD_CRON = 'crontab -r'
CREATE_VENV = 'virtualenv venv'
SRC_VENV = 'source venv/bin/activate'
DEPLOY   = '/home/pi/venv/bin/pip install git+https://github.com/EricFalkenberg/VVaaS'
SETUP_CRON = 'echo "30 12 * * * /home/pi/venv/bin/order_vv {0} {1}" | crontab -'

def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def exec_remote(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout:
        print line,
    for line in stderr:
        print line,

def scp_file(client, path):
    with SCPClient(client.get_transport()) as scp:
        click.echo('Sending {0} to remote host'.format(path))
        scp.put(path, remote_path='/home/pi/')

@click.command()
@click.argument('from_number')
@click.argument('to_number')
@click.argument('twilio_cfg', type=click.Path(exists=True, resolve_path=True))
@click.argument('ip')
def cli(from_number, to_number, twilio_cfg, ip):
    """
    Deploy VVaaS to the specified Raspberry Pi host 
    """
    click.echo('Accessing Remote Host')
    pi_pass = getpass.getpass(prompt='Raspberry Pi Password: ', stream=None)
    client = create_ssh_client(ip, DEFAULT_SSH_PORT, RPI_USERNAME, pi_pass) 
    exec_remote(client, APT_UPDATE) 
    exec_remote(client, APT_INSTALL)
    exec_remote(client, VENV_INSTALL)
    exec_remote(client, RM_OLD_VENV)
    exec_remote(client, RM_OLD_CRON)
    exec_remote(client, CREATE_VENV)
    exec_remote(client, SRC_VENV)
    exec_remote(client, DEPLOY)
    exec_remote(client, SETUP_CRON)
    scp_file(client, twilio_cfg) 

if __name__ == '__main__':
    cli()
