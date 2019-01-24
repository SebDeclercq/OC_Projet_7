#!/usr/bin/env python3
'''
@note       This test file'll contain all unit tests used to code due
            to the use of TDD as main methodology and to test code evolution
            for the app.wikipedia.Wikipedia class.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-20) : init
'''
from typing import List, Sequence, Tuple
from unittest import mock
import pytest
import app.wikipedia
from app.google_maps import Position

class Params:
    '''Class holding params for parametrized tests'''
    geosearch: Sequence[Tuple[Position, List[str]]] = (
        (Position(50.2934211, 2.7787176), ['Arras', 'Hôtel de Ville, Arras']),
    )

class TestWikipedia:
    '''Class testing the app.wikipedia.Wikipedia'''
    @pytest.mark.parametrize('position, expected_list', Params.geosearch)
    def test_wikipedia_geosearch(
            self, position: Position, expected_list: List[str]
    ) -> None:
        wikipedia: app.wikipedia.Wikipedia = app.wikipedia.Wikipedia()
        list_results: List[str] = wikipedia.geosearch(position)
        assert list_results[:2] == expected_list
