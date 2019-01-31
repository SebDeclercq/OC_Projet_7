#!/usr/bin/env python3
'''
@note       Main class for the GrandPy Website
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-31) : init
'''
from typing import Optional
import json
import os
from flask import Flask, jsonify, Response, render_template, request
from flask.json import JSONEncoder
from flask_bootstrap import Bootstrap
from app import app, google_maps
from dataclasses import asdict


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
        self.grandpy: app.App = app.App()

    def _define_routes(self) -> Response:
        '''Sets the routes up'''
        @self.app.route('/', methods=['GET'])
        def index() -> str:
            return render_template('index.html.j2')

        @self.app.route('/ask-grandpy', methods=['POST'])
        def ask_grandpy() -> Response:
            query: str = request.form['query']
            app_resp: Optional[app.Response] = self.grandpy.search(query)
            if app_resp:
                return jsonify(asdict(app_resp)), 200
            else:
                return jsonify({"summary": "Je n'ai pas compris"}), 404
