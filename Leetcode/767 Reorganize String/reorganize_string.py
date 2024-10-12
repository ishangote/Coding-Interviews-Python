import unittest
from collections import Counter
import heapq


def get_max_frequent_char(char_count, previous):
    if previous:
        return max(
            {
                char: count
                for char, count in char_count.items()
                if char != previous and count > 0
            },
            key=char_count.get,
            default="",
        )

    return max(char_count, key=char_count.get)


# Time: O(n^2), where n => number of characters in input string
# * Given that input_string only has lowercase letters => Time: O(26n) ~ O(n)
# Space: O(n)
# * Given that input_string only has lowercase letters => Space: O(1)
def reorganize_string_hash_map(input_string):
    char_count = Counter(input_string)
    res = []

    max_freq_char = get_max_frequent_char(char_count, "")
    while max_freq_char:
        res.append(max_freq_char)
        char_count[max_freq_char] -= 1

        max_freq_char = get_max_frequent_char(char_count, max_freq_char)

    return "".join(res) if len(res) == len(input_string) else ""


# ------------------------------------------------------ #


# * For generic question where characters are not limited to lowercase letters
# Time: O(n x logn), where n => number of characters in input string
# Space: O(n)
def reorganize_string_heap(input_string):
    char_count = Counter(input_string)
    max_heap = [(count * -1, char) for char, count in char_count.items()]
    res = []

    heapq.heapify(max_heap)
    previous = None

    while max_heap or previous:
        if previous and not max_heap:
            return ""

        count, max_freq_char = heapq.heappop(max_heap)
        res.append(max_freq_char)
        count += 1

        if previous:
            heapq.heappush(max_heap, previous)
            previous = None

        if count != 0:
            previous = (count, max_freq_char)

    return "".join(res)


class TestReorganizeString(unittest.TestCase):
    def test_get_max_frequent_char(self):
        self.assertEqual(get_max_frequent_char({"a": 3, "b": 1, "c": 1}, ""), "a")
        self.assertEqual(get_max_frequent_char({"a": 2, "b": 1, "c": 1}, "a"), "b")
        self.assertEqual(get_max_frequent_char({"a": 2, "b": 0, "c": 0}, "a"), "")

    def test_reorganize_string_hash_map(self):
        self.assertEqual(reorganize_string_hash_map("aaabc"), "abaca")
        self.assertEqual(reorganize_string_hash_map("aaab"), "")

    def test_reorganize_string_heap(self):
        self.assertEqual(reorganize_string_heap("aaabc"), "abaca")
        self.assertEqual(reorganize_string_heap("aaab"), "")


if __name__ == "__main__":
    unittest.main()
