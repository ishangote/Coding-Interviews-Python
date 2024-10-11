import sys
import unittest


# Time: O(n + m), where n => length of list1, m => length of list2
# Space: O(min(n, m))
def minimum_index_sum(list1, list2):
    min_idx_sum, res = sys.maxsize, []

    smaller_list = list1 if len(list1) <= len(list2) else list2
    larger_list = list1 if smaller_list == list2 else list2

    smaller_list_idx_map = {char: idx for idx, char in enumerate(smaller_list)}

    for idx, char in enumerate(larger_list):
        if char in smaller_list_idx_map:
            if idx + smaller_list_idx_map[char] < min_idx_sum:
                min_idx_sum = idx + smaller_list_idx_map[char]
                res = [char]

            elif idx + smaller_list_idx_map[char] == min_idx_sum:
                res.append(char)

            else:
                continue

    return res


class TestMinimumIndexSum(unittest.TestCase):
    def test_minimum_index_sum(self):
        self.assertEqual(
            minimum_index_sum(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                [
                    "Piatti",
                    "The Grill at Torrey Pines",
                    "Hungry Hunter Steakhouse",
                    "Shogun",
                ],
            ),
            ["Shogun"],
        )

        self.assertEqual(
            minimum_index_sum(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KFC", "Shogun", "Burger King"],
            ),
            ["Shogun"],
        )

        self.assertEqual(
            minimum_index_sum(["happy", "sad", "good"], ["sad", "happy", "good"]),
            ["sad", "happy"],
        )


if __name__ == "__main__":
    unittest.main()
