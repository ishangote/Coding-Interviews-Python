import unittest


# Time: O(n), where n => length of input_string
# Space: O(1)
def number_of_segments(input_string):
    whitespace = " "
    idx, res = 0, 0

    while True:
        if idx >= len(input_string):
            break

        if idx < len(input_string) and input_string[idx] == whitespace:
            while idx < len(input_string) and input_string[idx] == whitespace:
                idx += 1

        if idx < len(input_string) and input_string[idx] != whitespace:
            res += 1
            while idx < len(input_string) and input_string[idx] != whitespace:
                idx += 1

    return res


class TestNumberOfSegments(unittest.TestCase):
    def test_number_of_segments(self):
        self.assertEqual(number_of_segments("   "), 0)
        self.assertEqual(number_of_segments("helloworld"), 1)
        self.assertEqual(number_of_segments(" hello   world"), 2)
        self.assertEqual(number_of_segments(" hello   world   "), 2)


if __name__ == "__main__":
    unittest.main()
