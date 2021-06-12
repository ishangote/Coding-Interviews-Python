import unittest
from generate_document import generate_document

class TestGenerateDocument(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(True, generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
        self.assertEqual(False, generate_document("A", "a"))
        self.assertEqual(True, generate_document("a hsgalhsa sanbjksbdkjba kjx", ""))
        self.assertEqual(True, generate_document("aheaollabbhb", "hello"))
        self.assertEqual(False, generate_document("Bste!hetsi ogEAxpert", "AlgoExpert is the Best!"))

if __name__ == "__main__": unittest.main()