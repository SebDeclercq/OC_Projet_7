'''
@note       Main script to launch the GrandPy website
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-02-15) : init
'''
from flask import Flask
from website import website


site: website.Website = website.Website()
app: Flask = site.app
