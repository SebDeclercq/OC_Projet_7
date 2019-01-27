#!/usr/bin/env python3
'''
@note       Module containing the class querying the Wikipedia API.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-24) : init
'''
from typing import List, Optional
import mediawiki
from app import google_maps


class Wikipedia:
    '''Class connecting to the Wikipedia API and offers a search
    method to retrieve a MediaWikiPage content'''
    def __init__(self) -> None:
        '''Constructor'''
        self.client: mediawiki.MediaWiki = mediawiki.MediaWiki(lang='fr')

    def geosearch(self, position: google_maps.Position) -> List[str]:
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
        try:
            page: Optional[mediawiki.MediaWikiPage] = self.client.page(title)
        except mediawiki.exceptions.PageError:
            page = None
        return page
