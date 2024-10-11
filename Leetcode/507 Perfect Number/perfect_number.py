import unittest
from math import sqrt


# Time: O(sqrt(num))
# Space: O(1)
def perfect_number(num):
    if num < 5:
        return False

    sum = 1
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            sum += i + num // i

    return sum == num


class TestPerfectNumber(unittest.TestCase):
    def test_perfect_number(self):
        self.assertTrue(perfect_number(28))

        self.assertFalse(perfect_number(7))


if __name__ == "__main__":
    unittest.main()
