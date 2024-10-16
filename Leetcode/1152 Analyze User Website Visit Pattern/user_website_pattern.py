import unittest
from collections import defaultdict
from itertools import combinations


# Time: O(n^3), where n => number of websites
# Space: O(n^3)
def user_website_pattern(usernames, timestamps, websites):
    user_visits_map = defaultdict(list)

    for time, user, website in sorted(
        zip(timestamps, usernames, websites), key=lambda x: x[0]
    ):
        user_visits_map[user].append(website)

    pattern_scores = defaultdict(lambda: 0)
    for user, websites in user_visits_map.items():
        for pattern in set(combinations(websites, 3)):
            pattern_scores[pattern] += 1

    max_pattern, max_score = [], 0
    for pattern, score in pattern_scores.items():
        if score > max_score or (score == max_score and pattern < max_pattern):
            max_pattern = pattern
            max_score = score

    return list(max_pattern)


class TestUserWebsitePattern(unittest.TestCase):
    def test_user_website_pattern(self):
        self.assertEqual(
            user_website_pattern(
                [
                    "joe",
                    "joe",
                    "joe",
                    "james",
                    "james",
                    "james",
                    "james",
                    "mary",
                    "mary",
                    "mary",
                ],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [
                    "home",
                    "about",
                    "career",
                    "home",
                    "cart",
                    "maps",
                    "home",
                    "home",
                    "about",
                    "career",
                ],
            ),
            ["home", "about", "career"],
        )

        self.assertEqual(
            user_website_pattern(
                ["ua", "ua", "ua", "ub", "ub", "ub"],
                [1, 2, 3, 4, 5, 6],
                ["a", "b", "a", "a", "b", "c"],
            ),
            ["a", "b", "a"],
        )


if __name__ == "__main__":
    unittest.main()
