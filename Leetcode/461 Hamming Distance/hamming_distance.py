import unittest


# Time: O(1), since x, y can be at most 32 bit
# Space: O(1)
def hamming_distance(x, y):
    res = 0

    while x or y:
        res += (x ^ y) % 2
        x >>= 1
        y >>= 1

    return res


class TestHammingDistance(unittest.TestCase):
    def test_hamming_distance(self):
        self.assertEqual(hamming_distance(3, 1), 1)
        self.assertEqual(hamming_distance(1, 4), 2)
        self.assertEqual(hamming_distance(3, 4), 3)


if __name__ == "__main__":
    unittest.main()
