import unittest


# Time: O(log(n))
# Space: O(1)
def power_of_two_brute_force(n):
    if n == 0:
        return False

    while n % 2 == 0:
        n = n // 2

    return n == 1


# Time: O(1)
# Space: O(1)
def power_of_two_bit(n):
    return n > 0 and (n & (n - 1)) == 0


class TestPowerOfTwo(unittest.TestCase):
    def test_power_of_two_bf(self):
        self.assertEqual(power_of_two_brute_force(16), True)
        self.assertEqual(power_of_two_brute_force(5), False)

    def test_power_of_two_bit(self):
        self.assertEqual(power_of_two_bit(16), True)
        self.assertEqual(power_of_two_bit(5), False)


if __name__ == "__main__":
    unittest.main()
