#!/usr/bin/env python3
'''
@note       Main class for the GrandPy Website
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-31) : init
'''
import os
from flask import Flask, Response, render_template


class Website:
    '''Main class for the GrandPy Website

    Params:
        template_folder Where to put the jinja2 templates
        app The Flask application
    '''
    def __init__(self) -> None:
        '''Constructor'''
        self.template_folder: str = os.environ.get(
            'TEMPLATE_FOLDER', '../website/templates/'
        )
        self.app: Flask = Flask(__name__, template_folder=self.template_folder)
        self._define_routes()

    def _define_routes(self) -> Response:
        '''Sets the routes up'''
        @self.app.route('/', methods=['GET'])
        def index() -> str:
            return render_template('index.html')
