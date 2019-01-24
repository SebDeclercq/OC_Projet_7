#!/usr/bin/env python3
'''
@note       This test file'll contain all unit tests used to code due
            to the use of TDD as main methodology and to test code evolution
            for the app.parser.Parser class.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-20) : init
'''
from typing import Optional, Sequence, Tuple
import pytest
import app.google_maps


@pytest.fixture
def google_maps() -> app.google_maps.GoogleMaps:
    '''Fixture instanciating a GoogleMaps object'''
    return app.google_maps.GoogleMaps()


class Params:
    '''Class holding params for parametrized tests'''
    api_queries_and_results: Sequence[
        Tuple[str, Optional[Tuple[float, float]]]] = (
            ('adresse mairie arras', (50.2934211, 2.7787176)),
            ('beffroi arras', (50.2911244, 2.7769304)),
            ('boulangerie achicourt', (50.2724255, 2.7561987)),
            ('citadelle lille', (50.6409299, 3.0445812)),
            ('citadelle arras', (50.2827966, 2.7600242)),
            # "random data for fake search" in base64
            ('cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo', None),
        )


class TestGoogleMaps:
    '''Class testing the app.google_maps.GoogleMaps'''
    @pytest.mark.parametrize('search_terms, position',
                             Params.api_queries_and_results)
    def test_search_geocode(
            self, search_terms: str, position: Optional[Tuple[float, float]],
            google_maps: app.google_maps.GoogleMaps
    ) -> None:
        '''Checks that geocode() returns an instance of Position
        with the expected latitude/longitude'''
        result: Optional[app.google_maps.Position] = google_maps.geocode(
            search_terms
        )
        if position:
            assert isinstance(result, app.google_maps.Position)
            assert result == app.google_maps.Position(*position)
        else:
            assert result is None
