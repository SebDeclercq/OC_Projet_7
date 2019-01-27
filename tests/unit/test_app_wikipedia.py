#!/usr/bin/env python3
'''
@note       This test file'll contain all unit tests used to code due
            to the use of TDD as main methodology and to test code evolution
            for the app.wikipedia.Wikipedia class.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-20) : init
'''
from typing import List, Optional, Sequence, Tuple
from unittest import mock
import mediawiki
import pytest
from app import google_maps, wikipedia


@pytest.fixture
def wiki(monkeypatch: None) -> wikipedia.Wikipedia:
    '''Fixture instanciating a Wikipedia object'''
    wiki_mock: mock.Mock = mock.Mock()
    wiki_mock.return_value = None
    monkeypatch.setattr('mediawiki.MediaWiki.__init__', wiki_mock)
    return wikipedia.Wikipedia()


class Params:
    '''Class holding params for parametrized tests'''
    geosearch: Sequence[Tuple[google_maps.Position, List[str]]] = (
        (google_maps.Position(50.2934211, 2.7787176), [
            'Hôtel Les Trois Luppars',
            "Grand-Place d'Arras",
            'Chapelle des Chariottes',
        ]),
        (google_maps.Position(50.2911244, 2.7769304), [
            "Beffroi d'Arras",
            "Hôtel de ville d'Arras",
            'Place des Héros (Arras)',
        ]),
        (google_maps.Position(50.2724255, 2.7561987), [
            'Achicourt', "Gare d'Achicourt"
        ]),
        (google_maps.Position(50.6409299, 3.0445812), [
            'Citadelle de Lille',
            'Les Poussins, Parc de la Citadelle',
            'Esplanade du Champ de Mars (Lille)'
        ]),
        (google_maps.Position(50.2827966, 2.7600242), [
            'Main Square Festival',
            "Citadelle d'Arras", "Faubourg d'Amiens British Cemetery, "
            "The Arras Mémorial And The Flying Services Mémorial"
        ]),
        (google_maps.Position(0., 20.), []),
    )
    page_search: Sequence[Tuple[str, Optional[str]]] = (
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
        # "random data for fake search" in base64
        ('cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo', None),
    )


class TestWikipedia:
    '''Class testing the app.wikipedia.Wikipedia'''
    @pytest.mark.parametrize('position, expected_list', Params.geosearch)
    def test_wikipedia_geosearch(
            self, position: google_maps.Position, expected_list: List[str],
            wiki: wikipedia.Wikipedia, monkeypatch: None
    ) -> None:
        '''Checks that Wikipedia returns the exact expected results (3)'''
        geosearch_mock: mock.Mock = mock.Mock()
        geosearch_mock.return_value = expected_list
        monkeypatch.setattr('mediawiki.MediaWiki.geosearch', geosearch_mock)
        list_results: List[str] = wiki.geosearch(position)
        assert list_results == expected_list

    @pytest.mark.parametrize('title, summary_50_char', Params.page_search)
    def test_wikipedia_get_page(
            self, title: str, summary_50_char: Optional[str],
            wiki: wikipedia.Wikipedia, monkeypatch: None
    ) -> None:
        '''Checks that the page search returns the expected summary
        (50 first characters)'''
        page_mock: mock.Mock = mock.Mock()
        page_mock.return_value = None
        # Mocking MediaWikiPage (usually returned by .page())
        monkeypatch.setattr('mediawiki.MediaWikiPage.__init__', page_mock)
        page_search_mock: mock.Mock = mock.Mock()
        if summary_50_char is not None:
            # Mocking property w/ expected return value
            summary_mock: mock.PropertyMock = mock.PropertyMock()
            summary_mock.return_value = summary_50_char
            monkeypatch.setattr('mediawiki.MediaWikiPage.summary',
                                summary_mock)
            page_search_mock.return_value = mediawiki.MediaWikiPage()
        else:
            page_search_mock.return_value = None
        # Mocking .page()
        monkeypatch.setattr('mediawiki.MediaWiki.page', page_search_mock)
        page = wiki.page_search(title)
        if summary_50_char is not None:
            assert isinstance(page, mediawiki.MediaWikiPage)
            assert page.summary[:49] == summary_50_char
        else:
            assert page is None
