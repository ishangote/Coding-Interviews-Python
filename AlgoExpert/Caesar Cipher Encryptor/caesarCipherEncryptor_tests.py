import unittest
from caesarCipherEncryptor import caesarCipherEncryptor

class CaesarCipherEncryptor(unittest.TestCase):
    def test_generic(self):
        self.assertEqual("zab", caesarCipherEncryptor("xyz", 2))
        self.assertEqual("abc", caesarCipherEncryptor("abc", 0))
        self.assertEqual("def", caesarCipherEncryptor("abc", 3))
        self.assertEqual("abc", caesarCipherEncryptor("abc", 26))
        self.assertEqual("abc", caesarCipherEncryptor("abc", 52))
        self.assertEqual("hvtepmjpjpnnkwyykyhgpel", caesarCipherEncryptor("iwufqnkqkqoolxzzlzihqfm", 25))

if __name__ == "__main__": unittest.main()