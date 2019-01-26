#!/usr/bin/env python3
'''
@note       Module containing the class querying the Wikipedia API.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-24) : init
'''
from typing import List
import mediawiki
from app.google_maps import Position


class Wikipedia:
    '''Class connecting to the Wikipedia API and offers a search
    method to retrieve a MediaWikiPage content'''
    def __init__(self) -> None:
        '''Constructor'''
        self.client: mediawiki.mediawiki.MediaWiki = mediawiki.MediaWiki(
            lang='fr'
        )

    def geosearch(self, position: Position) -> List[str]:
        '''Performs a geosearch on the Wikipedia API
        Params:
            position: used to get GPS data for the search
        Returns:
            A list of results (title pages from wikipedia)'''
        return self.client.geosearch(
            str(position.latitude), str(position.longitude),
            results=3
        )

    def page_search(self, title: str) -> mediawiki.MediaWikiPage:
        '''Performs a page search on the Wikipedia API
        Params:
            title: the title of the page to collect
        Returns:
            An instance of MediaWikiPage'''
        return self.client.page(title)
