import unittest


# Time: O(n x m), where n => number of words, m => max length of word
# Space: O(1)
def valid_word_square(words):
    for r in range(len(words)):
        for c in range(len(words[r])):
            if c >= len(words) or r >= len(words[c]) or words[r][c] != words[c][r]:
                return False

    return True


class TestValidWordSquare(unittest.TestCase):
    def test_valid_word_square(self):
        self.assertEqual(valid_word_square(["abcd", "bnrt", "crmy", "dtye"]), True)
        self.assertEqual(valid_word_square(["abcd", "bnrt", "crm", "dt"]), False)


if __name__ == "__main__":
    unittest.main()
