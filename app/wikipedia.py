#!/usr/bin/env python3
from typing import List
import mediawiki
from app.google_maps import Position


class Wikipedia:
    def __init__(self) -> None:
        self.client: mediawiki.mediawiki.MediaWiki = mediawiki.MediaWiki()

    def geosearch(self, position: Position) -> List[str]:
        return self.client.geosearch(
            str(position.latitude), str(position.longitude)
        )

    
