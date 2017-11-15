#!/usr/bin/python
import click
import subprocess
from twilio.rest import Client
import configparser
import time
import logging

FORMAT = '%(asctime)-15s %(user)s %(message)s'
conf = { 'user' : 'order_vv' }

def get_twilio_acct(fname):
    config = configparser.ConfigParser()
    config.read(fname)
    return map(lambda id: config.get('account', id), ['sid', 'auth'])

@click.command()
@click.argument('from_number')
@click.argument('to_number')
@click.argument('twilio_cfg', type=click.Path(exists=True))
def cli(from_number, to_number, twilio_cfg):
    """
    Order a Vegan Volcano over the phone. 
    """
    sid, auth = get_twilio_acct(twilio_cfg)
    client = Client(sid, auth)
    call = client.api.account.calls.create(to="+1{0}".format(to_number),
                                           from_="+1{0}".format(from_number),
                                           url="https://handler.twilio.com/twiml/EHf4c9c85b46cfcc78964ccb63e640cb04")
    logging.basicConfig(format=FORMAT, filename='vvaas.log', level=logging.INFO)
    logger = logging.getLogger('VVaaS')
    logger.info(call.sid, extra=conf)

if __name__ == '__main__':
    cli()

