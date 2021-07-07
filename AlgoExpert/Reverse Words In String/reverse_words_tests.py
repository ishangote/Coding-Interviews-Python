import unittest
from reverse_words import reverse_words

class TestReverseWordsInString(unittest.TestCase):
    def setUp(self) -> None:
        self.strings = ["AlgoExpert is the best!", "Reverse These Words", " ", "words, separated, by, commas", "APPLE PEAR PLUM ORANGE"]
        self.reversed_strings = ["best! the is AlgoExpert", "Words These Reverse", " ", "commas by, separated, words,", "ORANGE PLUM PEAR APPLE"]
    
    def test_generic(self):
        for idx, s in enumerate(self.strings):
            self.assertEqual(self.reversed_strings[idx], reverse_words(s))

if __name__ == "__main__": unittest.main()