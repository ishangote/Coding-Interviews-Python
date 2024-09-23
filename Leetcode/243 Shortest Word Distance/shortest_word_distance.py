import unittest
import sys


# Time: O(n * m), where n => length of words_dict
# and m => length of word1 + length of word2 (comparing strings takes O(m))
# Space: O(1)
def shortest_word_distance(words_dict, word1, word2):
    idx1, idx2 = -1, -1
    min_distance = sys.maxsize

    for idx, word in enumerate(words_dict):
        if word == word1:
            idx1 = idx

        if word == word2:
            idx2 = idx

        if idx1 != -1 and idx2 != -1:
            min_distance = min(min_distance, abs(idx1 - idx2))

    return min_distance


class TestShortestWordDistance(unittest.TestCase):
    def test_shortest_word_distance(self):
        self.assertEqual(
            shortest_word_distance(
                ["practice", "makes", "perfect", "coding", "makes"],
                "coding",
                "practice",
            ),
            3,
        )

        self.assertEqual(
            shortest_word_distance(
                ["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"
            ),
            1,
        )


if __name__ == "__main__":
    unittest.main()
