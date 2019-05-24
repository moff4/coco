from unittest import TestCase

from generator.brick import *


class WordTest(TestCase):
    def test_word_init(self):
        word = Word("anY")
        self.assertEqual(word.string, 'any')

    def test_word(self):
        results = list(Word("Difficult").mutate())
        self.assertEqual(4, len(results))
        self.assertIn('DIFFICULT', results)
        self.assertIn('Difficult', results)
        self.assertIn('dIfFiCuLt', results)

    def test_strange_word(self):
        results = list(Word("stranger").mutate())
        self.assertIn('Stranger', results)
        self.assertIn('STRANGER', results)
        self.assertIn('sTrAnGeR', results)
        self.assertIn('$tranger', results)
        self.assertIn('stranger', results)
        self.assertIn('str@nger', results)
        self.assertIn('$tr@nger', results)







