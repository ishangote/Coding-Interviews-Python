import unittest


# Time: O(n), where n => length of input string
# Space: O(n)
def count_binary_substrings(input_string):
    idx, counts = 0, []

    while idx < len(input_string):
        runner = idx

        while runner < len(input_string) and input_string[runner] == input_string[idx]:
            runner += 1

        counts.append(runner - idx)
        idx = runner

    res = 0

    for idx in range(1, len(counts)):
        res += min(counts[idx - 1], counts[idx])

    return res


class TestCountBinarySubstrings(unittest.TestCase):
    def test_count_binary_substrings(self):
        self.assertEqual(count_binary_substrings("0101"), 3)
        self.assertEqual(count_binary_substrings("001110"), 3)
        self.assertEqual(count_binary_substrings("00110011"), 6)


if __name__ == "__main__":
    unittest.main()
