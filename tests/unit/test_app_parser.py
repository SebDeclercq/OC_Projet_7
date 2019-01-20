#!/usr/bin/env python3
'''
@note       This test file'll contain all unit tests used to code due
            to the use of TDD as main methodology and to test code evolution
            for the app.parser.Parser class.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-20) : init
'''
from typing import List, Sequence, Tuple
import pytest
from app import parser


class Params:
    '''Class sharing reusable values for tests'''
    sentences: Sequence[Tuple[str, List[str]]] = (
        ('Ma super phrase de test', ['ma', 'super', 'phrase', 'de', 'test']),
        ('ET UNE AUTRE', ['et', 'une', 'autre']),
        ('encore une !', ['encore', 'une']),
        ('aVeC-Des CaractÈres_SpÉciaux:-)',
         ['avec', 'des', 'caractères', 'spéciaux'])
    )


class TestParser:
    '''Class testing the app.parser.Parser'''

    @pytest.mark.parametrize('sentence, list_of_words', Params.sentences)
    def test_parser_split_sentence(
            self, sentence: str, list_of_words: Sequence[str]
    ) -> None:
        '''Checks that parser correctly splits sentences into words'''
        assert parser.Parser.split_words(sentence) == list_of_words
