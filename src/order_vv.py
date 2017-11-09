#!/usr/bin/python
import click
import subprocess

@click.command()
@click.argument('number')
def cli(number):
    """
    Order a Vegan Volcano over the phone. 
    """
    click.echo("Not yet implemented")

if __name__ == '__main__':
    cli()

