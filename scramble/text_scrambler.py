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


class TextScrambler():

    def __init__(self, text):
        self.text = text

    def scramble(self):
        """Runs the scramble script on the given file"""
        return self._scramble_words(self._get_words(self.text))

    def _get_words(self, text):
        """Retuns all words in the contents of the given file name,
        as a list of lists."""
        return [line.split() for line in text.splitlines()]

    def _scramble_words(self, words):
        """Scrambles the words and returns a list
        of tuples, with the scrambled letters of the words.
        """
        def scramble_line(line):
            return " ".join([self._scramble(word) for word in line])

        return "\n".join([scramble_line(line) for line in words])

    def _scramble(self, word):
        """Scrambles the middle of a word, leaving first and last letters."""
        def has_number():
            return re.search(r"\d", word)

        def is_short(word_):
            return len(word_) < 2

        def rejoin_letters(*parts):
            return "".join(parts)

        pos = self._positions(word)
        text = word[slice(*pos)]
        if is_short(text) or has_number():
            return word
        return rejoin_letters(word[:pos[0]], self._permutate(text), word[pos[1]:])

    def _positions(self, word):
        """Returns the indeces for first and last letter, not counting
        non-word characters.
        """
        groups = re.search(r"(\W*)(\w*)(\W*)", word).groups()
        return 1 + len(groups[0]), - len(groups[2]) - 1

    def _permutate(self, word):
        """Permutates the word and returns a random pick of all permutations."""
        perms = permutations(word)
        pick = randint(1, math.factorial(len(word)) - 1)
        next(perms)
        for _ in range(1, min(pick, 1_000_000)):
            next(perms)
        return "".join(next(perms))
