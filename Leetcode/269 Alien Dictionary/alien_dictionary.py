import unittest
from collections import defaultdict


def make_graph(words):
    graph = defaultdict(set)
    in_degree = {}
    for word in words:
        for ch in word:
            in_degree[ch] = 0

    for first_word, second_word in zip(words, words[1:]):
        for ch1, ch2 in zip(first_word, second_word):
            if ch1 != ch2:
                # Very important => [za, zb, ca, cb] => a->b edge should not be added twice to in_degree! Hence...
                if ch2 not in graph[ch1]:
                    graph[ch1].add(ch2)
                    in_degree[ch2] += 1
                break
        else:
            # Invalid if second_word is a strict prefix of first_word (e.g., ["abc", "ab"])
            # This runs only if all characters match before length comparison.
            if len(second_word) < len(first_word):
                return []

    return [graph, in_degree]


def topological_sort(graph, in_degree):
    stack = [vertex for vertex in in_degree if in_degree[vertex] == 0]
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node)
        for nbr in graph[node]:
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                stack.append(nbr)

    for vertex in in_degree:
        if in_degree[vertex] > 0:
            return ""

    return "".join(ans)


# Time: O(C + V + E), where C => total number of characters in words(stored in graph), V => vertices (number of unique characters), E => number of edges
# Space: O(C)
def alien_dictionary(words):
    graph = make_graph(words)
    return topological_sort(graph[0], graph[1]) if graph else ""


class TestAlienDictionary(unittest.TestCase):
    def test_make_graph(self):
        self.assertEqual(
            make_graph(["za", "zb", "ca", "cb"]),
            [{"a": {"b"}, "z": {"c"}}, {"a": 0, "b": 1, "c": 1, "z": 0}],
        )

    def test_alien_order(self):
        self.assertEqual(
            alien_dictionary(["wrt", "wrf", "er", "ett", "rfttzmn"]), "nmzwertf"
        )
        self.assertEqual(alien_dictionary(["x", "z"]), "xz")
        self.assertEqual(alien_dictionary(["x", "z", "x"]), "")

        self.assertEqual(alien_dictionary(["ab", "abc"]), "cba")
        self.assertEqual(alien_dictionary(["abc", "ab"]), "")

        self.assertEqual(alien_dictionary(["za", "zb", "ca", "cb"]), "abzc")


if __name__ == "__main__":
    unittest.main()
