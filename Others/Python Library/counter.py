"""
"""

from collections import Counter
def counter(input):
    return Counter(input)

def most_common(input):
    counter = Counter(input)
    return counter.most_common(1)[0][0]

import unittest
class TestCounter(unittest.TestCase):
    def test_counter(self):
        # Input as string
        self.assertEqual(counter("hello"), {"h": 1, "e": 1, "l": 2, "o": 1})
        # Input as list
        self.assertEqual(counter(["hello", "world", "hello", "there"]), {"hello": 2, "world": 1, "there": 1})

    def test_most_common(self):
        # Input as string
        self.assertEqual(most_common("hello"), 'l')

        # Input as list
        self.assertEqual(most_common(["hello", "world", "hello", "there"]), "hello")

if __name__ == "__main__": unittest.main()
