"""
Scramble Text

Scrambles the middle of a word or words of a text,
read from a file on disk.

@author: Gus Garcia
"""
import re
from itertools import permutations
from random import randint
from os.path import isfile
import math


def run_scramble(file_name):
    """Runs the scramble script on the given file"""
    return scramble_words(get_words(file_name))


def get_words(file_name):
    """Retuns all words in the contents of the given file name,
    as a list of lists."""
    return [split_line(line) for line in fetch_text(file_name)]


def fetch_text(file_name):
    """Fetches the raw text from the given file name"""
    if isfile(file_name):
        with open(file_name) as original_text:
            return original_text.readlines()
    return []


def split_line(line):
    """Splits a line into a list of words, separator as space."""
    return line.split() if line else []


def scramble_words(words):
    """Scrambles the words and returns a list
    of tuples, with the scrambled letters of the words.
    """
    return "\n".join([" ".join([scramble(word) for word in line]) for line in words])


def scramble(word):
    """Scrambles the middle of a word, leaving first and last letters."""
    def has_number():
        return re.search(r"\d", word)

    def is_short(word_):
        return len(word_) < 2

    pos = _positions(word)
    text = word[slice(*pos)]
    if is_short(text) or has_number():
        return word
    return "{}{}{}".format(word[:pos[0]], _permutate(text), word[pos[1]:])


def _positions(word):
    """Returns the indeces for first and last letter, not counting
    non-word characters.
    """
    groups = re.search(r"(\W*)(\w*)(\W*)", word).groups()
    return 1 + len(groups[0]), - len(groups[2]) - 1


def _permutate(word):
    """Permutates the word and returns a random pick of all permutations."""
    perms = permutations(word)
    pick = randint(1, math.factorial(len(word)) - 1)
    next(perms)
    for _ in range(1, min(pick, 1_000_000)):
        next(perms)
    return "".join(next(perms))
