#!/usr/bin/env python3
'''
@note       This test file'll contain all unit tests used to code due
            to the use of TDD as main methodology and to test code evolution
            for the app.wikipedia.Wikipedia class.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-20) : init
'''
from typing import List, Sequence, Tuple
import mediawiki
import pytest
import app.wikipedia
from app.google_maps import Position


@pytest.fixture
def wikipedia() -> app.wikipedia.Wikipedia:
    '''Fixture instanciating a Wikipedia object'''
    return app.wikipedia.Wikipedia()


class Params:
    '''Class holding params for parametrized tests'''
    geosearch: Sequence[Tuple[Position, List[str]]] = (
        (Position(50.2934211, 2.7787176), [
            'Hôtel Les Trois Luppars',
            "Grand-Place d'Arras",
            'Chapelle des Chariottes',
        ]),
        (Position(50.2911244, 2.7769304), [
            "Beffroi d'Arras",
            "Hôtel de ville d'Arras",
            'Place des Héros (Arras)',
        ]),
        (Position(50.2724255, 2.7561987), ['Achicourt', "Gare d'Achicourt"]),
        (Position(50.6409299, 3.0445812), [
            'Citadelle de Lille',
            'Les Poussins, Parc de la Citadelle',
            'Esplanade du Champ de Mars (Lille)'
        ]),
        (Position(50.2827966, 2.7600242), [
            'Main Square Festival',
            "Citadelle d'Arras", "Faubourg d'Amiens British Cemetery, ",
            "The Arras Mémorial And The Flying Services Mémorial"
        ]),
    )
    page_search: Sequence[Tuple[str, str]] = (
        ("Hôtel Les Trois Luppars",
         '''L'hôtel Les Trois Luppars est un établissement hô'''),
        ("Beffroi d'Arras",
         '''Le beffroi d'Arras est un ouvrage de charpente de'''),
        ("Achicourt",
         '''Achicourt est une commune française située dans l'''),
        ("Citadelle de Lille",
         '''La citadelle de Lille est un ouvrage militaire bâ'''),
        ("Main Square Festival",
         '''Le Main Square Festival est un festival de musiqu'''),
    )


class TestWikipedia:
    '''Class testing the app.wikipedia.Wikipedia'''
    @pytest.mark.parametrize('position, expected_list', Params.geosearch)
    def test_wikipedia_geosearch(
            self, position: Position, expected_list: List[str],
            wikipedia: app.wikipedia.Wikipedia
    ) -> None:
        '''Checks that Wikipedia returns the exact expected results (3)'''
        list_results: List[str] = wikipedia.geosearch(position)
        assert list_results == expected_list

    @pytest.mark.parametrize('title, summary_50_char', Params.page_search)
    def test_wikipedia_get_page(
            self, title: str, summary_50_char: str,
            wikipedia: app.wikipedia.Wikipedia
    ) -> None:
        '''Checks that the page search returns the expected summary
        (50 first characters)'''
        page = wikipedia.page_search(title)
        assert isinstance(page, mediawiki.MediaWikiPage)
        assert page.summary[:49] == summary_50_char
