from unittest import TestCase

from generator.brick import *


class WordTest(TestCase):
    def test_word_init(self):
        word = Word("anY")
        self.assertEqual(word.string, 'any')

    def test_word(self):
        word = Word("Difficult")
        results = word.mutate()
        self.assertEqual(results, [])







