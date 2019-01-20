#!/usr/bin/env python3
'''
@note Module containing the class parsing user input for Google Maps
      and Wikipedia APIs querying
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-20) : init
'''
from typing import List
import re


class Parser:
    '''Class parsing user input for Google Maps and Wikipedia APIs querying'''
    @classmethod
    def split_words(cls, sentence: str) -> List[str]:
        '''Class method splitting sentences to a list of words'''
        list_of_words: List[str] = re.split(r'[\W_]+', sentence.lower())
        return [s for s in list_of_words if s]
