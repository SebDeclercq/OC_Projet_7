#!/usr/bin/env python3
'''
@note       Main class for the App
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-27) : init
'''
from typing import List, Optional
import mediawiki
from dataclasses import dataclass
from app import parser, google_maps, wikipedia


@dataclass
class Response:
    '''Container-like class for App Responses handling'''
    title: str
    coord: google_maps.Position
    summary: str


class App:
    '''Main class for the App'''
    def __init__(self) -> None:
        '''Constructor'''
        self.parser: parser.Parser = parser.Parser()
        self.google_maps: google_maps.GoogleMaps = google_maps.GoogleMaps()
        self.wikipedia: wikipedia.Wikipedia = wikipedia.Wikipedia()

    def search(self, query: str) -> Optional[Response]:  # pylint: disable=R1710
        '''Simple entry for search with the App
        Params:
            The user search
        Returns:
            The Response from the App'''
        query = self._parse_query(query)
        if query:
            location: Optional[google_maps.Position] = self._find_coords(query)
            if location is not None:
                page: Optional[mediawiki.MediaWikiPage] = \
                    self._query_wikipedia(location)
                if page is not None:
                    return Response(
                        title=page.title,
                        coord=location,
                        summary=page.summary
                    )

    def _parse_query(self, query) -> str:  # pylint: disable=R1710
        '''Private method interacting with the parser'''
        query = self.parser.clean_sentence(query)
        return self.parser.find_useful_info(query)

    def _find_coords(self, query: str) -> google_maps.Position:
        '''Private method interacting with the Google Maps API'''
        return self.google_maps.geocode(query)

    def _query_wikipedia(
            self, location: google_maps.Position
    ) -> Optional[mediawiki.MediaWikiPage]:
        '''Private method interacting with the Wikipedia API'''
        titles: List[str] = self.wikipedia.geosearch(location)
        if titles:
            return self.wikipedia.page_search(titles[0])
