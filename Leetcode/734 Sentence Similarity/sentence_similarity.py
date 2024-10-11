import unittest
from collections import defaultdict


# Time: O(n), where n => length of sentence1/2
# Space: O(m), where m => length of similar pairs
def sentence_similarity(sentence1, sentence2, similar_pairs):
    if len(sentence1) != len(sentence2):
        return False

    similar_words_map = defaultdict(set)
    for [word1, word2] in similar_pairs:
        similar_words_map[word1].add(word2)
        similar_words_map[word2].add(word1)

    for word1, word2 in zip(sentence1, sentence2):
        if word1 == word2:
            continue

        if word1 not in similar_words_map or word2 not in similar_words_map:
            return False

        if (
            word1 not in similar_words_map[word2]
            or word2 not in similar_words_map[word1]
        ):
            return False

    return True


class TestSentenceSimilarity(unittest.TestCase):
    def test_sentence_similarity(self):
        self.assertTrue(
            sentence_similarity(
                ["great", "acting", "skills"],
                ["fine", "drama", "talent"],
                [["great", "fine"], ["drama", "acting"], ["skills", "talent"]],
            )
        )
        self.assertTrue(sentence_similarity(["great"], ["great"], []))

        self.assertTrue(
            sentence_similarity(
                ["an", "extraordinary", "meal"],
                ["one", "good", "dinner"],
                [
                    ["great", "good"],
                    ["extraordinary", "good"],
                    ["well", "good"],
                    ["wonderful", "good"],
                    ["excellent", "good"],
                    ["fine", "good"],
                    ["nice", "good"],
                    ["any", "one"],
                    ["some", "one"],
                    ["unique", "one"],
                    ["the", "one"],
                    ["an", "one"],
                    ["single", "one"],
                    ["a", "one"],
                    ["truck", "car"],
                    ["wagon", "car"],
                    ["automobile", "car"],
                    ["auto", "car"],
                    ["vehicle", "car"],
                    ["entertain", "have"],
                    ["drink", "have"],
                    ["eat", "have"],
                    ["take", "have"],
                    ["fruits", "meal"],
                    ["brunch", "meal"],
                    ["breakfast", "meal"],
                    ["food", "meal"],
                    ["dinner", "meal"],
                    ["super", "meal"],
                    ["lunch", "meal"],
                    ["possess", "own"],
                    ["keep", "own"],
                    ["have", "own"],
                    ["extremely", "very"],
                    ["actually", "very"],
                    ["really", "very"],
                    ["super", "very"],
                ],
            )
        )

        self.assertFalse(
            sentence_similarity(
                ["great"], ["doubleplus", "good"], [["great", "doubleplus"]]
            )
        )


if __name__ == "__main__":
    unittest.main()
