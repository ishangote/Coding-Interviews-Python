import unittest


# Time: O(1)
# Space: O(1)
def alternating_bits(num):
    tmp = num ^ (num >> 1)
    return tmp & (tmp + 1) == 0


class TestAlternatingBits(unittest.TestCase):
    def test_alternating_bits(self):
        self.assertTrue(alternating_bits(5))
        self.assertTrue(alternating_bits(10))

        self.assertFalse(alternating_bits(7))
        self.assertFalse(alternating_bits(11))


if __name__ == "__main__":
    unittest.main()
