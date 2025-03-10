import unittest


def recursive_helper_memo(idx, sentence, memo, input_string, word_set):
    if idx == len(input_string):
        return [""]

    if idx in memo:
        return memo[idx]

    memo[idx] = []
    for start in range(idx, len(input_string)):
        prefix = input_string[idx : start + 1]

        if prefix in word_set:
            suffix_sentences = (
                recursive_helper_memo(
                    start + 1,
                    sentence + " " + prefix,
                    memo,
                    input_string,
                    word_set,
                )
                if idx != 0
                else recursive_helper_memo(
                    start + 1, sentence + prefix, memo, input_string, word_set
                )
            )

            for suf in suffix_sentences:
                if suf:
                    memo[idx].append(f"{prefix} {suf}")
                else:
                    memo[idx].append(prefix)

    return memo[idx]


def recursive_helper(idx, sentence, res, input_string, word_set):
    if idx == len(input_string):
        res.append(sentence)
        return

    for start in range(idx, len(input_string)):
        prefix = input_string[idx : start + 1]

        if prefix in word_set:
            if idx != 0:
                recursive_helper(
                    start + 1, sentence + " " + prefix, res, input_string, word_set
                )
            else:
                recursive_helper(
                    start + 1, sentence + prefix, res, input_string, word_set
                )


def word_break_ii_top_down(input_string, word_dict):
    return recursive_helper_memo(0, "", {}, input_string, set(word_dict))


class TestWordBreakII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(
            word_break_ii_top_down("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
            ["cat sand dog", "cats and dog"],
        )
        self.assertEqual(
            word_break_ii_top_down(
                "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
            ),
            ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"],
        )
        self.assertEqual(
            word_break_ii_top_down("catsandog", ["cats", "dog", "sand", "and", "cat"]),
            [],
        )


if __name__ == "__main__":
    unittest.main()
