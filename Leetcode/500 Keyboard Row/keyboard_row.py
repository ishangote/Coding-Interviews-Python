import unittest


def is_word_in_row(word, row):
    for char in word:
        if char.lower() in row:
            continue
        return False

    return True


# Time: O(n x m), where n => length of words, m => length of word in words
# Space: O(1)
def keyboard_row(words):
    first_row = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
    second_row = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
    third_row = {"z", "x", "c", "v", "b", "n", "m"}

    res = []

    for word in words:
        if word[0].lower() in first_row and is_word_in_row(word, first_row):
            res.append(word)

        if word[0].lower() in second_row and is_word_in_row(word, second_row):
            res.append(word)

        if word[0].lower() in third_row and is_word_in_row(word, third_row):
            res.append(word)

    return res


class TestKeyboardRow(unittest.TestCase):
    def test_keyboard_row(self):
        self.assertEqual(
            keyboard_row(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"]
        )

        self.assertEqual(keyboard_row(["omk"]), [])

        self.assertEqual(keyboard_row(["adsdf", "sfd"]), ["adsdf", "sfd"])

        self.assertEqual(keyboard_row(["a", "b"]), ["a", "b"])


if __name__ == "__main__":
    unittest.main()
