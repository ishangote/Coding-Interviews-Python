import unittest


# Time: O(m + n), where m => length of word1, n => length of word2
# Space: O(1)
def merge_strings_alternately(word1, word2):
    pt1, pt2 = 0, 0
    res = ""

    while pt1 < len(word1) and pt2 < len(word2):
        res += f"{word1[pt1]}{word2[pt2]}"
        pt1 += 1
        pt2 += 1

    while pt1 < len(word1):
        res += word1[pt1]
        pt1 += 1

    while pt2 < len(word2):
        res += word2[pt2]
        pt2 += 1

    return res


class TestMergeStringsAlternately(unittest.TestCase):
    def test_merge_strings_alternately(self):
        self.assertEqual(merge_strings_alternately("abc", "pqr"), "apbqcr")
        self.assertEqual(merge_strings_alternately("ab", "pqrs"), "apbqrs")
        self.assertEqual(merge_strings_alternately("abcd", "pq"), "apbqcd")


if __name__ == "__main__":
    unittest.main()
