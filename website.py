'''
@note       Main script to launch the GrandPy website
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-31) : init
'''
from flask import Flask
from ui import website


def create_app() -> Flask:
    '''Flask Application Factory'''
    site: website.Website = website.Website()
    return site.app


if __name__ == '__main__':
    create_app()
