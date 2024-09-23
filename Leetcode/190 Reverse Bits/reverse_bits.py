import unittest


# Time: O(1)
# Space: O(1)
def reverse_bits(n):
    res = 0

    for itr in range(32):
        bit = (n >> itr) & 1
        res = res | (bit << (31 - itr))

    return res


class TestReverseBits(unittest.TestCase):
    def test_reverse_bits(self):
        self.assertEqual(reverse_bits(43261596), 964176192)
        self.assertEqual(reverse_bits(4294967293), 3221225471)


if __name__ == "__main__":
    unittest.main()
