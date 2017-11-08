#!/usr/bin/python
import click
import subprocess

@click.command()
@click.argument('number')
def cli(number):
    """
    Deploy VVaaS to the specified Raspberry Pi host 
    """
    click.echo("Not yet implemented")

if __name__ == '__main__':
    cli()

