#!/usr/bin/env python3
'''
@note       This test file'll contain all unit tests used to code due
            to the use of TDD as main methodology and to test code evolution
            for the website.website class.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-31) : init
@version    0.0.1 (2019-02-08) : debugged test_index()
'''
import pytest
from flask import Response, testing
from website import website


@pytest.fixture(scope='class', autouse=True)
def client() -> testing.FlaskClient:
    '''Fixture setting the flask environment up for testing'''
    test_website = website.Website()
    with test_website.app.app_context():
        yield test_website.app.test_client()


class TestWebsite:
    '''Test suite for the Website class'''
    def test_index(self, client: testing.FlaskClient) -> None:
        '''Checks that the index route returns what is expected'''
        r: Response = client.get('/')
        assert r.status_code == 200
        assert r.headers['Content-Type'] == 'text/html; charset=utf-8'
        text_excerpt: str = 'Salut mon gars !'
        assert text_excerpt in r.get_data().decode('utf-8')
