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
    """TextScrambler. Only one method is public. To run the application:

    In [1]: from scrambler.text_scrambler import TextScrambler
    In [2]: TextScrambler("Some text").scramble()
    Out[2]: "Smoe txet"

    The text may contain line breaks and special characters.
    """

    def __init__(self, text):
        self.text = text

    def scramble(self):
        """Runs the scramble app on the text assigned to the constructor."""

        def scramble_line(line):
            return " ".join([self._scramble(word) for word in line])

        def is_valid_object():
            return isinstance(self, TextScrambler) and isinstance(self.text, str)

        if not is_valid_object():
            return None
        lines = [line.split() for line in self.text.splitlines()]
        return "\n".join([scramble_line(line) for line in lines])

    def _scramble(self, word):
        """Scrambles the middle of a word, leaving first and last letters."""

        def word_has_number():
            return re.search(r"\d", word)

        def text_is_short():
            return len(text) < 2

        def rejoin_letters(*parts):
            return "".join(parts)

        pos = self._positions(word)
        text = word[slice(*pos)]
        if text_is_short() or word_has_number():
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
