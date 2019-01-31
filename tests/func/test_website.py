#!/usr/bin/env python3
'''
@note       This test file'll contain all functional tests for the Website.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-31) : init
'''
from typing import Any, Dict, Sequence, Tuple
import json
import pytest
from flask import Response, testing
from website import website


@pytest.fixture(scope='class', autouse=True)
def client() -> testing.FlaskClient:
    '''Fixture setting the flask environment up for testing'''
    test_website = website.Website()
    with test_website.app.app_context():
        yield test_website.app.test_client()


class Params:
    searches: Sequence[Tuple[str, int, Dict[str, Any]]] = (
        ('Où se trouve le furet du nord de Lille ?', 200, {
            'title': 'Colonne de la Déesse',
            'coord': {
                'latitude': 50.6366327, 'longitude': 3.0629882
            },
            'summary': 'La colonne de la déesse est un monument commémora'
        }),
        ("Bonjour ! Trouve-moi l'adresse de la mairie d'Arras, stp !", 200, {
            'title': 'Hôtel Les Trois Luppars',
            'coord': {
                'latitude': 50.2934211, 'longitude': 2.7787176
            },
            'summary': "L'hôtel Les Trois Luppars est un établissement hô"
        }),
        # "random data for fake search" in base64
        ('cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo', 404,
            {"summary": "Je n'ai pas compris"}
        ),
    )


class TestWebsite:
    @pytest.mark.parametrize('query, expected_code, dict_resp',
                             Params.searches)
    def test_ask_grandpy(
            self, query: str, expected_code: int,
            dict_resp: Dict[str, Any], client: testing.FlaskClient
    ) -> None:
        '''Checks that posting data to the website returns the
        expected result'''
        r: Response = client.post('/ask-grandpy', data={
            'query': query
        })
        assert r.status_code == expected_code
        r_content: Dict[str, Any] = r.get_json()
        r_content['summary'] = r_content['summary'][:49]
        assert dict_resp == r_content
