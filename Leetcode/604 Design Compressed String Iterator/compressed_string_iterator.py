import unittest


class StringIteratorBruteForce:
    def __init__(self, compressed_string):
        self.compressed_string = compressed_string
        self.iterator = 0
        self.stack = []

    # Time: O(n), where n => length of compressed string
    # Space: O(m), where m => maximum number of repetitions of a character
    def next(self):
        if self.stack:
            return self.stack.pop()

        if not self.hasNext():
            return " "

        char = self.compressed_string[self.iterator]

        runner = self.iterator + 1
        while (
            runner < len(self.compressed_string)
            and self.compressed_string[runner].isdigit()
        ):
            runner += 1
        repetition = int(self.compressed_string[self.iterator + 1 : runner])

        self.stack.extend([char] * repetition)
        self.iterator = runner

        return self.stack.pop()

    # Time: O(1)
    # Space: O(1)
    def hasNext(self):
        return self.stack or self.iterator < len(self.compressed_string)


class StringIteratorOptimized:
    def __init__(self, compressed_string):
        self.compressed_string = compressed_string
        self.iterator = 0
        self.current_character = ""
        self.current_character_count = 0

    # Time: O(n), where n => length of compressed string
    # Space: O(1)
    def next(self):
        if not self.hasNext():
            return " "

        if self.current_character_count > 0:
            self.current_character_count -= 1
            return self.current_character

        # Get current character
        self.current_character = self.compressed_string[self.iterator]
        runner = self.iterator + 1

        # Find where the number ends
        while (
            runner < len(self.compressed_string)
            and self.compressed_string[runner].isdigit()
        ):
            runner += 1

        # Update iterator to point after the current character and its count
        self.current_character_count = int(
            self.compressed_string[self.iterator + 1 : runner]
        )
        self.iterator = runner  # Move iterator to the next character

        # Decrease count by one since we're returning one occurrence of the character
        self.current_character_count -= 1
        return self.current_character

    # Time: O(1)
    # Space: O(1)
    def hasNext(self):
        return self.current_character_count > 0 or self.iterator < len(
            self.compressed_string
        )


class TestStringIterator(unittest.TestCase):
    def test_string_iterator(self):
        string_iterator = StringIteratorBruteForce("L1e2t1C1o1d1e1")

        self.assertEqual(string_iterator.next(), "L")
        self.assertEqual(string_iterator.next(), "e")
        self.assertEqual(string_iterator.next(), "e")
        self.assertEqual(string_iterator.next(), "t")
        self.assertEqual(string_iterator.next(), "C")
        self.assertEqual(string_iterator.next(), "o")

        self.assertTrue(string_iterator.hasNext())

        self.assertEqual(string_iterator.next(), "d")

        self.assertTrue(string_iterator.hasNext())

        self.assertEqual(string_iterator.next(), "e")

        self.assertFalse(string_iterator.hasNext())

        self.assertEqual(string_iterator.next(), " ")

    def test_string_iterator_optimized(self):
        string_iterator_optimized = StringIteratorOptimized("L1e2t1C1o1d1e1")

        self.assertEqual(string_iterator_optimized.next(), "L")
        self.assertEqual(string_iterator_optimized.next(), "e")
        self.assertEqual(string_iterator_optimized.next(), "e")
        self.assertEqual(string_iterator_optimized.next(), "t")
        self.assertEqual(string_iterator_optimized.next(), "C")
        self.assertEqual(string_iterator_optimized.next(), "o")

        self.assertTrue(string_iterator_optimized.hasNext())

        self.assertEqual(string_iterator_optimized.next(), "d")

        self.assertTrue(string_iterator_optimized.hasNext())

        self.assertEqual(string_iterator_optimized.next(), "e")

        self.assertFalse(string_iterator_optimized.hasNext())

        self.assertEqual(string_iterator_optimized.next(), " ")


if __name__ == "__main__":
    unittest.main()
