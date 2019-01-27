#!/usr/bin/env python3
'''
@note       Simple console interface to GrandPy
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-27) : init
'''
import click
from app import app


@click.command()
@click.option('--query', prompt="What's your question ?\t",
              help='The question used for searching in the App')
def grandpy(query: str) -> app.Response:
    '''Simple console UI for the GrandPy App, your favorite
    story teller :-)'''
    my_app: app.App = app.App()
    click.echo(my_app.search(query))


if __name__ == '__main__':
    grandpy()
