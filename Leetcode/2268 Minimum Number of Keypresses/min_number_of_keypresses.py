import unittest
from collections import Counter


# Time: O(n), where n => length of input string
# Space: O(1)
def min_number_of_keypresses(input_string):
    char_count = Counter(input_string)

    res = 0
    keypresses = 0

    for idx, freq in enumerate(sorted(char_count.values(), reverse=True)):
        if idx % 9 == 0:
            keypresses += 1

        res += freq * keypresses

    return res


class TestMinimumNumberOfKeypresses(unittest.TestCase):
    def test_min_number_of_keypresses(self):
        self.assertEqual(min_number_of_keypresses("apple"), 5)
        self.assertEqual(min_number_of_keypresses("abcdefghijkl"), 15)


if __name__ == "__main__":
    unittest.main()
