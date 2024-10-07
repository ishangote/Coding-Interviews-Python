import unittest


# Time: O(n), where n => length of word
# Space: O(1)
def detect_capital(word):
    return word.islower() or word.isupper() or word.istitle()


class TestDetectCapital(unittest.TestCase):
    def test_detect_capital(self):
        self.assertEqual(detect_capital("USA"), True)
        self.assertEqual(detect_capital("leetcode"), True)
        self.assertEqual(detect_capital("Google"), True)

        self.assertEqual(detect_capital("FlaG"), False)


if __name__ == "__main__":
    unittest.main()
