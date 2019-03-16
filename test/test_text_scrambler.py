"""
Unit tests for the TextScrambler class.
"""
import re
import pytest
from scramble.text_scrambler import TextScrambler


@pytest.fixture
def scrambler():
    return TextScrambler()


def test_scramble_empty_string(scrambler):
    assert scrambler.scramble("") == "" 


def test_scramble_empty_nothing(scrambler):
    assert scrambler.scramble(None) is None 


def test_scramble_1_letter_word(scrambler):
    assert scrambler.scramble("a") == "a" 


def test_scramble_2_letter_word(scrambler):
    assert scrambler.scramble("ab") == "ab" 


def test_scramble_3_letter_word(scrambler):
    assert scrambler.scramble("abc") == "abc" 


def test_scramble_word(scrambler):
    assert scrambler.scramble("abcd") == "acbd" 


def test_scramble_words(scrambler):
    text = """Hello world!
    From Down Under"""
    assert scrambler.scramble(text) != text
    assert re.match(f"[{text}]{{{len(text)}}}", text)
