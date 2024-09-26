import unittest


# Time: O(n), where n => length of input_string
# Space: O(1)
def is_subsequence(subsequence, input_string):
    subseq_idx = 0

    for char in input_string:
        if subseq_idx == len(subsequence):
            break

        if char != subsequence[subseq_idx]:
            continue

        subseq_idx += 1

    return subseq_idx == len(subsequence)


class TesIsSubsequence(unittest.TestCase):
    def test_is_subsequence(self):
        self.assertTrue(is_subsequence("abc", "abc"))
        self.assertTrue(is_subsequence("abc", "ahbgdc"))
        self.assertTrue(is_subsequence("a", "abc"))

        self.assertFalse(is_subsequence("abc", "cba"))
        self.assertFalse(is_subsequence("abcx", "efabcd"))


if __name__ == "__main__":
    unittest.main()
