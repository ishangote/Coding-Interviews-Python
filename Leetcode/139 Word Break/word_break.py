import unittest


def recursive_helper(input_string, word_set, memo):
    if input_string in memo:
        return memo[input_string]

    if not input_string:
        return True

    for idx in range(1, len(input_string) + 1):
        prefix = input_string[:idx]
        if prefix in word_set and recursive_helper(input_string[idx:], word_set, memo):
            memo[input_string] = True
            return True

    memo[input_string] = False
    return False


# Time: O(n^2), where n => length of input string
# Space: O(n)
def word_break_top_down(input_string, word_dict):
    return recursive_helper(input_string, set(word_dict), {})


# ---------------------------------------------------------------------------- #


class TestWordBreak(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(word_break_top_down("leetcode", ["leet", "code"]), True)
        self.assertEqual(
            word_break_top_down("thequickbrownfox", ["the", "quick", "fox", "brown"]),
            True,
        )
        self.assertEqual(
            word_break_top_down(
                "bedbathandbeyond", ["bed", "bath", "bedbath", "and", "away"]
            ),
            False,
        )
        self.assertEqual(
            word_break_top_down(
                "bedbathandbeyond", ["teddy", "bath", "bedbath", "and", "beyond"]
            ),
            True,
        )
        self.assertEqual(
            word_break_top_down("catsandog", ["cats", "dog", "sand", "and", "cat"]),
            False,
        )
        self.assertEqual(
            word_break_top_down(
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                [
                    "a",
                    "aa",
                    "aaa",
                    "aaaa",
                    "aaaaa",
                    "aaaaaa",
                    "aaaaaaa",
                    "aaaaaaaa",
                    "aaaaaaaaa",
                    "aaaaaaaaaa",
                ],
            ),
            False,
        )


if __name__ == "__main__":
    unittest.main()
