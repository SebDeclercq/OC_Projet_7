#!/usr/bin/env python3
'''
@note       Main class for the GrandPy Website
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-31) : init
@version    0.0.2 (2019-02-08) : better error handling
@version    0.0.3 (2019-02-15) : escaping HTML Wikipedia response
'''
from typing import List, Optional
import html
import random
import os
from flask import Flask, jsonify, Response, render_template, request
from flask_bootstrap import Bootstrap
from app import app
from dataclasses import asdict


class Website:
    '''Main class for the GrandPy Website

    Params:
        app The Flask application
        boostrap Adds Bootstrap to the App
        wrong_query_answers_file The file containing the fake answers
        wrong_query_answers List of answers to render when GrandPy was
                            unable to retrieve a real answer
    '''
    def __init__(self) -> None:
        '''Constructor'''
        self.app: Flask = Flask(__name__)
        self.bootstrap: Bootstrap = Bootstrap(self.app)
        self.wrong_query_answers_file: str = 'wrong_query_answers.yml'
        self._get_wrong_query_answers()
        self._define_routes()
        self.grandpy: app.App = app.App()

    def _get_wrong_query_answers(self) -> List[str]:
        file: str = os.path.join(
            os.path.dirname(__file__), self.wrong_query_answers_file
        )
        with open(file, encoding='utf-8') as answers:
            self.wrong_query_answers: List[str] = answers.readlines()
        return self.wrong_query_answers

    def _define_routes(self) -> Response:
        '''Sets the routes up'''
        @self.app.route('/', methods=['GET'])
        def index() -> str:
            return render_template(
                'index.html.j2',
                google_public_api_key=os.environ.get('GOOGLE_PUBLIC_API_KEY')
            )

        @self.app.route('/ask-grandpy', methods=['POST'])
        def ask_grandpy() -> Response:
            query: str = request.form['query']
            app_resp: Optional[app.Response] = self.grandpy.search(query)
            if app_resp:
                app_resp.summary = html.escape(app_resp.summary, quote=False)
                app_resp.title = html.escape(app_resp.title, quote=False)
                return jsonify(asdict(app_resp)), 200
            else:
                answer: str = random.choice(self.wrong_query_answers).rstrip()
                return jsonify(
                    {"answer": html.escape(answer, quote=False)}
                ), 400
