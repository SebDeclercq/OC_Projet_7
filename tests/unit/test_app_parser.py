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
import app.parser


@pytest.fixture
def parser() -> app.parser.Parser:
    return app.parser.Parser()


class Params:
    '''Class sharing reusable values for tests'''
    sentences: Sequence[Tuple[str, List[str]]] = (
        ('Ma super phrase de test', ['ma', 'super', 'phrase', 'de', 'test']),
        ('ET UNE AUTRE', ['et', 'une', 'autre']),
        ('encore une !', ['encore', 'une']),
        ('aVeC-Des CaractÈres_SpÉciaux:-)',
         ['avec', 'des', 'caractères', 'spéciaux'])
    )
    no_stop_words: Sequence[Tuple[List[str], List[str]]] = (
        (['ma', 'super', 'phrase', 'de', 'test'], ['super', 'phrase', 'test']),
        (['et', 'une', 'autre'], []),
        (['encore', 'une'], []),
        (['avec', 'des', 'caractères', 'spéciaux'], ['caractères', 'spéciaux'])
    )


class TestParser:
    '''Class testing the app.parser.Parser'''

    @pytest.mark.parametrize('sentence, list_of_words', Params.sentences)
    def test_parser_split_sentence(
            self, sentence: str, list_of_words: Sequence[str],
            parser: app.parser.Parser
    ) -> None:
        '''Checks that the parser correctly splits sentences into words'''
        assert parser.split_words(sentence) == list_of_words


    @pytest.mark.parametrize('list_of_words, no_stop_words', Params.no_stop_words)
    def test_remove_stop_words(
            self, list_of_words: List[str], no_stop_words: List[str],
            parser: app.parser.Parser
    ) -> None:
        '''Checks that the parser correctly removes the stop words'''
        assert parser.remove_stop_words(list_of_words) == no_stop_words
