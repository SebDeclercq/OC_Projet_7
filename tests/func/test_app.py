#!/usr/bin/env python3
'''
@note       This test file'll contain all functional tests for the App.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-26) : init
'''
from typing import Sequence, Tuple
import pytest
from app import app, google_maps


@pytest.fixture
def test_app() -> app.App:
    return app.App()


class Params:
    '''Class holding params for parametrized tests'''
    end_to_end: Sequence[Tuple[str, app.Response]] = ((
        "Bonjour ! Trouve-moi l'adresse de la mairie d'Arras, stp !",
        app.Response(
            title='Hôtel Les Trois Luppars',
            coord=google_maps.Position(50.2934211, 2.7787176),
            summary='''L'hôtel Les Trois Luppars est un établissement hô''')
        ), (
        'salut, dis-moi où je pourrais trouver une boulangerie à Achicourt',
        app.Response(
            title='Achicourt',
            coord=google_maps.Position(50.2724255, 2.7561987),
            summary='''Achicourt est une commune française située dans l''')
        ), (
        "Localise-moi la citadelle de lille",
         app.Response(
            title='Citadelle de Lille',
            coord=google_maps.Position(50.6409299, 3.0445812),
            summary='''La citadelle de Lille est un ouvrage militaire bâ''')
        ),
    )


class TestApp:
    '''Class testing the app main class App'''
    @pytest.mark.parametrize('query, expected_resp', Params.end_to_end)
    def test_search(
            self, query: str, expected_resp: app.Response, test_app: app.App
    ) -> None:
        '''Checks that the search does provide the expected response'''
        resp: app.Response = test_app.search(query)
        resp.summary = resp.summary[:49]
        assert resp == expected_resp
