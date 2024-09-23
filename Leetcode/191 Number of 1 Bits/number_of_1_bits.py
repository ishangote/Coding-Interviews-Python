import unittest


# Time: O(1), since n is a 32-bit integer
# Space: O(1)
def number_of_1_bits(n):
    n = int(n, 2)
    m = int("0" * 31 + "1", 2)

    count = 0

    while n:
        count += n & m
        n = n >> 1

    return count


class TestNumberOf1Bits(unittest.TestCase):
    def test_number_of_1_bits(self):
        self.assertEqual(number_of_1_bits("101001"), 3)
        self.assertEqual(number_of_1_bits("101011"), 4)
        self.assertEqual(number_of_1_bits("100000001"), 2)


if __name__ == "__main__":
    unittest.main()
