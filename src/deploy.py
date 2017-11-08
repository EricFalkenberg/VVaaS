#!/usr/bin/python
import click
import subprocess

GET_BUILD_SCRIPT = """
    sudo pip install virtualenv;
    source venv/bin/activate;
    pip install git+https://github.com/EricFalkenberg/raspi_tools.git#egg=flash_sd;
    flash_sd --help;
    """

@click.command()
@click.argument('ip')
def cli(ip):
    """
    Deploy VVaaS to the specified Raspberry Pi host 
    """
    click.echo("Deploying VVaaS to pi@{0}".format(ip))
    subprocess.call(['ssh', 'pi@{0}'.format(ip), GET_BUILD_SCRIPT])

if __name__ == '__main__':
    cli()

