import unittest


# Time: : O(n^2) (due to the growing "a" * (idx + 1)), where n => number of words in the sentence
# Space: O(n)
def goat_latin(sentence):
    words = sentence.split()

    for idx, word in enumerate(words):
        if word[0].lower() not in "aeiou":
            word = word[1:] + word[0]

        word += "ma"
        word += "a" * (idx + 1)

        words[idx] = word

    return " ".join(words)


class TestGoatLatin(unittest.TestCase):
    def test_goat_latin(self):
        # Basic tests
        self.assertEqual(
            goat_latin("I speak Goat Latin"), "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        )
        self.assertEqual(
            goat_latin("The quick brown fox"), "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa"
        )

        # Edge cases
        self.assertEqual(goat_latin("a"), "amaa")  # Single vowel word
        self.assertEqual(goat_latin("z"), "zmaa")  # Single consonant word
        self.assertEqual(goat_latin("A"), "Amaa")  # Uppercase vowel single letter
        self.assertEqual(goat_latin("B"), "Bmaa")  # Uppercase consonant single letter
        self.assertEqual(goat_latin(""), "")  # Empty string
        self.assertEqual(
            goat_latin("goat latin"), "oatgmaa atinlmaaa"
        )  # Two words, both lowercase


if __name__ == "__main__":
    unittest.main()
