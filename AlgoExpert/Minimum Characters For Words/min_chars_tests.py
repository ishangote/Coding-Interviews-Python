import unittest
from min_chars import minimum_characters

class TestMinimumCharactersForWords(unittest.TestCase):
    def setUp(self) -> None:
        self.words = [["tim", "is", "great"], ["my", "coding", "skills", "are", "great"], ["this", "that", "did", "deed", "them!", "a"], ["mississippi", "piper", "icing", "ice", "pickle", "piping", "pie", "pi", "sassy", "serpent", "python", "ascii", "sister", "mister"]]
        self.chars = [["t", "i", "m", "s", "g", "r", "e", "a"], ["m", "y", "c", "o", "d", "i", "n", "g", "s", "s", "k", "l", "l", "a", "r", "e", "t"], ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"], ["a", "c", "e", "e", "g", "h", "i", "i", "i", "i", "k", "l", "m", "n", "o", "p", "p", "r", "s", "s", "s", "s", "t", "y"]]
    
    def test_generic(self):
        for i, w in enumerate(self.words):
            # test two lists order does not matter: assertCountEqual
            self.assertCountEqual(self.chars[i], minimum_characters(w))

if __name__ == "__main__": unittest.main()