import unittest


# Time: O(nlog3(n))
# Space: O(1)
def power_of_three(num):
    while num >= 3:
        if num % 3 != 0:
            return False
        num //= 3

    return num == 1


class TestPowerOfThree(unittest.TestCase):
    def test_power_of_three_edge(self):
        self.assertFalse(power_of_three(0))
        self.assertTrue(power_of_three(1))
        self.assertFalse(power_of_three(2))

    def test_power_of_three(self):
        self.assertTrue(power_of_three(27))
        self.assertTrue(power_of_three(81))
        self.assertFalse(power_of_three(-27))
        self.assertFalse(power_of_three(12))


"""
EDGE CASE 1

n = 0, n = 2
n % 3 => infinite loop
"""

"""
EDGE CASE 2

n = 1
return True as 3^0 = 1
"""

if __name__ == "__main__":
    unittest.main()
