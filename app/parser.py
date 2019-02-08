#!/usr/bin/env python3
'''
@note Module containing the class parsing user input for Google Maps
      and Wikipedia APIs querying
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-20) : init
'''
from typing import List
import re
from nltk.stem import snowball
import requests


class Parser:
    '''Class parsing user input for Google Maps and Wikipedia APIs querying

    Class Parameter:
        FRENCH_STOP_WORDS_DB: URL to an online french stop words list

    Parameter:
        stop_words: list of words to exclude from user input
        stemmer: an instance of FrenchStemmer form nltk used to find the
                 base form of a word in a sentence for better filtering
    '''
    FRENCH_STOP_WORDS_DB: str = 'https://raw.githubusercontent.com/6/stopwords-json/master/dist/fr.json'  # pylint: disable=C0301 # noqa
    LOCALIZATION_VERB_STEMS: List[str] = ['trouv', 'situ', 'montr', 'localis']

    def __init__(self) -> None:
        '''Constructor'''
        with requests.get(self.FRENCH_STOP_WORDS_DB) as stop_words_db:
            self.stop_words: List[str] = stop_words_db.json()
        self.stop_words.extend(['grandpy', 'stp'])
        self.stemmer: snowball.FrenchStemmer = snowball.FrenchStemmer()

    def split_words(self, sentence: str) -> List[str]:  # pylint: disable=R0201
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

    def find_useful_info(self, sentence: str) -> str:
        '''Method extracted valuable information to use for the search
        in Google Maps API'''
        search_sentence: str = ''
        tokens: List[str] = sentence.split()
        for token in tokens:
            stem: str = self.stemmer.stem(token)
            if stem in self.LOCALIZATION_VERB_STEMS:
                idx: int = tokens.index(token)
                search_sentence = ' '.join(tokens[idx + 1:])
                break
        if not search_sentence:
            search_sentence = sentence
        return search_sentence
