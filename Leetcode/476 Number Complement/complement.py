import unittest


# Time: O(1), since number is at most 32 bit
# Space: O(1)
def number_of_bits(num):
    bits = 0

    while num:
        bits += 1
        num >>= 1

    return bits


# Time: O(1)
# Space: O(1)
def complement(num):
    bits = number_of_bits(num)
    mask = (2**bits) - 1
    return num ^ mask


class TestNumberComplement(unittest.TestCase):
    def test_number_complement(self):
        self.assertEqual(complement(5), 2)
        self.assertEqual(complement(9), 6)


if __name__ == "__main__":
    unittest.main()
