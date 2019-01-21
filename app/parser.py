#!/usr/bin/env python3
'''
@note Module containing the class parsing user input for Google Maps
      and Wikipedia APIs querying
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-20) : init
'''
from typing import List
import re
import requests


class Parser:
    FRENCH_STOP_WORDS_DB: str = 'https://raw.githubusercontent.com/6/stopwords-json/master/dist/fr.json'

    '''Class parsing user input for Google Maps and Wikipedia APIs querying'''
    def split_words(self, sentence: str) -> List[str]:
        '''Method splitting a sentence to a list of words'''
        list_of_words: List[str] = re.split(r'[\W_]+', sentence.lower())
        return [s for s in list_of_words if s]

    def remove_stop_words(self, list_of_words: List[str]) -> List[str]:
        '''Method removing all french stop words from list of words'''
        with requests.get(self.FRENCH_STOP_WORDS_DB) as stop_words_db:
            stop_words: List[str] = stop_words_db.json()
        return [s for s in list_of_words if s not in stop_words]
