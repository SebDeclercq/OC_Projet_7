#!/usr/bin/env python3
'''
@note       This test file'll contain all unit tests used to code due
            to the use of TDD as main methodology and to test code evolution
            for the app.parser.Parser class.
@author     Sébastien Declercq <sdq@afnor.org>
@version    0.0.1 (2019-01-20) : init
'''
from typing import List, Sequence, Tuple
from unittest import mock
import pytest
import app.parser
from app import parser


@pytest.fixture
def test_parser() -> parser.Parser:
    '''Fixture instanciating a Parser object'''
    return parser.Parser()


class Params:
    '''Class sharing reusable values for tests'''
    raw_sentences: Sequence[Tuple[str, List[str], str]] = (
        ('Ma super phrase de test',
         ['ma', 'super', 'phrase', 'de', 'test'],
         'super phrase test'),
        ('ET UNE AUTRE', ['et', 'une', 'autre'], ''),
        ('encore une !', ['encore', 'une'], ''),
        ('aVeC-Des CaractÈres_SpÉciaux:-)',
         ['avec', 'des', 'caractères', 'spéciaux'],
         'caractères spéciaux'),
        ("Salut Grandpy ! Montre-moi où se trouve le beffroi d'Arras stp",
         ['salut', 'grandpy', 'montre', 'moi', 'où', 'se', 'trouve', 'le',
          'beffroi', 'd', 'arras', 'stp'],
         'salut montre trouve beffroi arras')
    )
    cleaned_up_sentences: Sequence[Tuple[str, str]] = (
        ('trouver adresse mairie arras', 'adresse mairie arras'),
        ('montre beffroi arras', 'beffroi arras'),
        ('situe siège afnor', 'siège afnor'),
        ('salut dis trouverait boulangerie achicourt',
         'boulangerie achicourt'),
        ('propose adresse localise citadelle lille', 'citadelle lille'),
    )


class TestParser:
    '''Class testing the app.parser.Parser'''
    @pytest.mark.parametrize('sentence, list_of_words, _',
                             Params.raw_sentences)
    def test_parser_split_sentence(
            self, sentence: str, list_of_words: List[str],
            _: List[str], test_parser: parser.Parser
    ) -> None:
        '''Checks that the parser correctly splits sentences into words'''
        assert test_parser.split_words(sentence) == list_of_words

    @pytest.mark.parametrize('_, list_of_words, no_stop_words',
                             Params.raw_sentences)
    def test_remove_stop_words(
            self, _: str, list_of_words: List[str],
            no_stop_words: str, test_parser: parser.Parser
    ) -> None:
        '''Checks that the parser correctly removes the stop words'''
        assert test_parser.remove_stop_words(
            list_of_words
        ) == no_stop_words.split()

    @pytest.mark.parametrize('sentence, list_of_words, clean_sentence',
                             Params.raw_sentences)
    def test_clean_sentence(
            self, sentence: str, list_of_words: List[str],
            clean_sentence: str, monkeypatch
    ) -> None:
        '''Checks that sentence is correctly cleaned by the parser'''
        split_mock: mock.Mock = mock.Mock()
        split_mock.return_value = list_of_words
        rm_stop_mock: mock.Mock = mock.Mock()
        rm_stop_mock.return_value = clean_sentence.split()
        monkeypatch.setattr('app.parser.Parser.split_words', split_mock)
        monkeypatch.setattr('app.parser.Parser.remove_stop_words', rm_stop_mock)
        test_parser: parser.Parser = parser.Parser()
        assert test_parser.clean_sentence(sentence) == clean_sentence

    @pytest.mark.parametrize('sentence, expected_sentence',
                             Params.cleaned_up_sentences)
    def test_find_useful_info(
            self, sentence: str, expected_sentence: str,
            test_parser: app.parser.Parser
    ) -> None:
        '''Checks that the parser doest extract the useful information
        from a cleaned up sentence'''
        assert test_parser.find_useful_info(sentence) == expected_sentence
