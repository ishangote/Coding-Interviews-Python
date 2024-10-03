import unittest


# Time: O(n), where n => length of word
# Space: O(1)
def valid_abbreviation(word, abbr):
    word_idx, abbr_idx = 0, 0

    while word_idx < len(word) and abbr_idx < len(abbr):
        if abbr[abbr_idx].isdigit():
            if abbr[abbr_idx] == "0":
                return False

            jumps = 0

            while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                jumps = jumps * 10 + int(abbr[abbr_idx])
                abbr_idx += 1

            word_idx += jumps

        else:
            if word[word_idx] != abbr[abbr_idx]:
                return False

            word_idx += 1
            abbr_idx += 1

    return word_idx == len(word) and abbr_idx == len(abbr)


class TestValidAbbreviation(unittest.TestCase):
    def test_edge_case(self):
        self.assertFalse(valid_abbreviation("a", "01"))

    def test_valid_abbreviation(self):
        self.assertTrue(valid_abbreviation("internationalization", "i12iz4n"))
        self.assertTrue(valid_abbreviation("internationalization", "i5a11o1"))

        self.assertFalse(valid_abbreviation("apple", "a2e"))


if __name__ == "__main__":
    unittest.main()
