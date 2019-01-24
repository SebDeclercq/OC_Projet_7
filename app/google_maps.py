#!/usr/bin/env python3
'''
@note Module containing the class querying the Google Maps API
      and a Position class used to store longitude/latitude for
      geocoded result.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-24) : init
'''
import os
from typing import Any, Dict, List, Optional
import googlemaps
from dataclasses import dataclass


@dataclass
class Position:
    '''Simple dataclass used to store the position of a geolocalized result'''
    latitude: float
    longitude: float


class GoogleMaps:
    '''Class connecting to the Google Maps API and offers a search
    method to retrieve Position of a request'''
    def __init__(self) -> None:
        '''Constructor'''
        self.client: googlemaps.Client = googlemaps.Client(
            key=os.environ.get('GOOGLE_API_KEY')
        )

    def geocode(self, query: str) -> Optional[Position]:  # pylint: disable=R1710
        '''Method used to search in the Google Maps API'''
        result: List[Dict[str, Any]] = self.client.geocode(query)
        if result:
            position: Dict[str, float] = result[0]['geometry']['location']
            return Position(position['lat'], position['lng'])
