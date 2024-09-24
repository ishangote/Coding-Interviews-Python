import unittest


# Time: O(n), where n => number of words in input_string
# Space: O(n)
def word_pattern(pattern, input_string):
    words = input_string.split()

    if len(pattern) != len(words):
        return False

    char_to_word, word_to_char = {}, {}

    for char, word in zip(pattern, words):
        if char in char_to_word and char_to_word[char] != word:
            return False

        if word in word_to_char and word_to_char[word] != char:
            return False

        char_to_word[char] = word
        word_to_char[word] = char

    return True


"""
** Important Edge Case **

Input:
pattern = "abba"
s = "dog dog dog dog"

* Need to maintain and check 2 maps: pattern character to word, and
* word to pattern

"""


class TestWordPattern(unittest.TestCase):
    def test_word_pattern(self):
        self.assertEqual(word_pattern("abba", "dog cat cat dog"), True)
        self.assertEqual(word_pattern("abba", "dog cat dog cat"), False)
        self.assertEqual(word_pattern("abba", "dog cat cat dog dog"), False)

    def test_word_pattern(self):
        self.assertEqual(word_pattern("abba", "dog dog dog dog"), False)


if __name__ == "__main__":
    unittest.main()
