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
    '''Class parsing user input for Google Maps and Wikipedia APIs querying

    Class Parameter:
        FRENCH_STOP_WORDS_DB: URL to an online french stop words list

    Parameter:
        stop_words: list of words to exclude from user input
    '''
    FRENCH_STOP_WORDS_DB: str = 'https://raw.githubusercontent.com/6/stopwords-json/master/dist/fr.json'  # pylint: disable=C0301

    def __init__(self) -> None:
        '''Constructor'''
        with requests.get(self.FRENCH_STOP_WORDS_DB) as stop_words_db:
            self.stop_words: List[str] = stop_words_db.json()
        self.stop_words.extend(['grandpy'])

    def split_words(self, sentence: str) -> List[str]:
        '''Method splitting a sentence to a list of words'''
        list_of_words: List[str] = re.split(r'[\W_]+', sentence.lower())
        return [s for s in list_of_words if s]

    def remove_stop_words(self, list_of_words: List[str]) -> List[str]:
        '''Method removing all french stop words from list of words'''
        return [s for s in list_of_words if s not in self.stop_words]

    def clean_sentence(self, sentence: str) -> str:
        '''Method cleaning user input string for further use in
           querying APIs'''
        list_of_words: List[str] = self.split_words(sentence)
        return ' '.join(self.remove_stop_words(list_of_words))
