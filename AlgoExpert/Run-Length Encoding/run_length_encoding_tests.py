import unittest
from run_length_encoding import run_length_encoding

class TestRunLengthEncoding(unittest.TestCase):
    def test_generic(self):
        self.assertEqual("9A4A2B4C2D", run_length_encoding("AAAAAAAAAAAAABBCCCCDD"))
        self.assertEqual("1a1A", run_length_encoding("aA"))
        self.assertEqual("1a1A1a1A5a1A3a4A1B3b4B", run_length_encoding("aAaAaaaaaAaaaAAAABbbbBBBB"))
        self.assertEqual("111A122B133C144D", run_length_encoding("1A2BB3CCC4DDDD"))
        self.assertEqual("8 9a9a9a9a9a4a", run_length_encoding("        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
        self.assertEqual("9;3;9'9'2'111273524142311s", run_length_encoding(";;;;;;;;;;;;''''''''''''''''''''1233333332222211112222111s"))

if __name__ == "__main__": unittest.main()