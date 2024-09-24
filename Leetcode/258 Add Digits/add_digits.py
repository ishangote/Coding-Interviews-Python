import unittest


def add_digits_brute_force(num):
    res = 0

    while num != 0 or res > 9:
        if num == 0:
            num = res
            res = 0

        res += num % 10
        num = num // 10

    return res


# Time: O(1)
# Space: O(1)
def add_digits_math(num):
    if num == 0:
        return 0

    return num % 9 if num % 9 != 0 else 9


class TestAddDigits(unittest.TestCase):
    def test_add_digits(self):
        self.assertEqual(add_digits_brute_force(0), 0)
        self.assertEqual(add_digits_brute_force(4), 4)
        self.assertEqual(add_digits_brute_force(924), 6)
        self.assertEqual(add_digits_brute_force(32), 5)

    def test_add_digits_math(self):
        self.assertEqual(add_digits_math(0), 0)
        self.assertEqual(add_digits_math(4), 4)
        self.assertEqual(add_digits_math(924), 6)
        self.assertEqual(add_digits_math(32), 5)


if __name__ == "__main__":
    unittest.main()
