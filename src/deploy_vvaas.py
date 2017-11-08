#!/usr/bin/python
import click
import subprocess

INSTALL_VVAAS = """
    sudo pip install virtualenv;
    source venv/bin/activate;
    pip install git+https://github.com/EricFalkenberg/VVaaS.git#egg=VVaaS;
    VVaaS --help;
    """

@click.command()
@click.argument('ip')
def cli(ip):
    """
    Deploy VVaaS to the specified Raspberry Pi host 
    """
    click.echo("Deploying VVaaS to pi@{0}".format(ip))
    subprocess.call(['ssh', 'pi@{0}'.format(ip), INSTALL_VVAAS])

if __name__ == '__main__':
    cli()

