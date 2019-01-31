#!/usr/bin/env python3
'''
@note       Main class for the GrandPy Website
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-31) : init
'''
import os
from flask import Flask, Response, render_template
from flask_bootstrap import Bootstrap


class Website:
    '''Main class for the GrandPy Website

    Params:
        app The Flask application
    '''
    def __init__(self) -> None:
        '''Constructor'''
        self.app: Flask = Flask(__name__)
        self.bootstrap: Bootstrap = Bootstrap(self.app)
        self._define_routes()

    def _define_routes(self) -> Response:
        '''Sets the routes up'''
        @self.app.route('/', methods=['GET'])
        def index() -> str:
            return render_template('index.html.j2')
