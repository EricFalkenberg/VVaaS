#!/usr/bin/python
import click
import subprocess

INSTALL_VVAAS = """
    sudo apt-get install python-pip;
    sudo apt-get install git;
    sudo pip install virtualenv;
    rm -r venv;
    crontab -r;
    virtualenv venv;
    source venv/bin/activate;
    pip install git+https://github.com/EricFalkenberg/VVaaS;
    echo "30 12 * * * /home/pi/venv/bin/order_vv {0} {1}" | crontab -;
    """

@click.command()
@click.argument('from_number')
@click.argument('to_number')
@click.argument('ip')
def cli(from_number, to_number, ip):
    """
    Deploy VVaaS to the specified Raspberry Pi host 
    """
    click.echo("Deploying VVaaS to pi@{0}".format(ip))
    install_script = INSTALL_VVAAS.format(from_number, to_number)
    subprocess.call(['ssh', 'pi@{0}'.format(ip), install_script])

if __name__ == '__main__':
    cli()

