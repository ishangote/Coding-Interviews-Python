import unittest


# Time: O(n), where n => length of bits
# Space: O(1)
def one_bit_two_bit(bits):
    idx = 0

    while idx < len(bits) - 1:
        idx = idx + 1 if bits[idx] == 0 else idx + 2

    return idx == len(bits) - 1 and bits[idx] == 0


class TestOneBitTwoBit(unittest.TestCase):
    def test_one_bit_two_bit(self):
        self.assertTrue(one_bit_two_bit([0]))
        self.assertTrue(one_bit_two_bit([1, 1, 1, 0, 0]))

        self.assertFalse(one_bit_two_bit([1, 1]))
        self.assertFalse(one_bit_two_bit([1, 1, 1, 0]))


if __name__ == "__main__":
    unittest.main()
