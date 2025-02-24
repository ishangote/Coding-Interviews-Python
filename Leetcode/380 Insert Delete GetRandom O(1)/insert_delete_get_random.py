import unittest
import random


class RandomizedSet:
    def __init__(self):
        self.index_map = {}
        self.data = []

    # Time: O(1)
    def insert(self, value):
        if value in self.index_map:
            return False

        self.data.append(value)
        self.index_map[value] = len(self.data) - 1
        return True

    # Time: O(1)
    def remove(self, value):
        if value not in self.index_map:
            return False

        index_to_remove = self.index_map[value]
        last_element = self.data[-1]

        self.data[index_to_remove] = last_element
        self.index_map[last_element] = index_to_remove

        self.data.pop()
        del self.index_map[value]

        return True

    # Time: O(1)
    def get_random(self):
        return random.choice(self.data)


class TestRandomizedSet(unittest.TestCase):
    def test_randomized_set(self):
        randomized_set = RandomizedSet()

        self.assertTrue(randomized_set.insert(4))
        self.assertFalse(randomized_set.insert(4))

        self.assertTrue(randomized_set.insert(3))
        self.assertTrue(randomized_set.insert(2))
        self.assertTrue(randomized_set.insert(1))

        self.assertTrue(randomized_set.remove(3))
        self.assertFalse(randomized_set.remove(3))

        self.assertTrue(randomized_set.get_random() in [4, 2, 1])

    def test_randomized_set_2(self):
        randomized_set = RandomizedSet()

        self.assertTrue(randomized_set.insert(0))
        self.assertTrue(randomized_set.insert(1))
        self.assertTrue(randomized_set.remove(0))
        self.assertTrue(randomized_set.insert(2))
        self.assertTrue(randomized_set.remove(1))

        self.assertTrue(randomized_set.get_random() in [2])


if __name__ == "__main__":
    unittest.main()
