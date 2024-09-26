import unittest


# Time: O(n), where n => length of s + t
# Space: O(1)
def find_difference(s, t):
    res = 0

    for char in s + t:
        res = res ^ ord(char)

    return chr(res)


class TestFindTheDifference(unittest.TestCase):
    def test_find_the_difference(self):
        self.assertEqual(find_difference("abcd", "abcde"), "e")
        self.assertEqual(find_difference("abcd", "aabcd"), "a")


if __name__ == "__main__":
    unittest.main()
