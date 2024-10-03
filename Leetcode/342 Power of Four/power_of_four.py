import unittest


def power_of_four(num):
    while num >= 4:
        if num % 4 != 0:
            return False
        num //= 4

    return num == 1


class TestPowerOfFour(unittest.TestCase):
    def test_power_of_four_edge(self):
        self.assertFalse(power_of_four(0))
        self.assertFalse(power_of_four(2))
        self.assertFalse(power_of_four(3))
        self.assertTrue(power_of_four(1))

    def test_power_of_four(self):
        self.assertTrue(power_of_four(16))
        self.assertFalse(power_of_four(5))


if __name__ == "__main__":
    unittest.main()
