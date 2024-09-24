import unittest


def ugly_number(num):
    if num <= 0:
        return False

    num = abs(num)

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        elif num % 3 == 0:
            num = num // 3
        elif num % 5 == 0:
            num = num // 5
        else:
            return False

    return True


class TestUglyNumber(unittest.TestCase):
    def test_ugly_number(self):
        self.assertEqual(ugly_number(0), False)
        self.assertEqual(ugly_number(1), True)
        self.assertEqual(ugly_number(6), True)
        self.assertEqual(ugly_number(8), True)
        self.assertEqual(ugly_number(60), True)
        self.assertEqual(ugly_number(14), False)
        self.assertEqual(ugly_number(-2147483648), False)


if __name__ == "__main__":
    unittest.main()
