import unittest


# Time: O(n), where n => length of num
# Space: O(1)
def strobogrammatic_number(num):
    lo, hi = 0, len(num) - 1

    reversed_digits = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}

    while lo <= hi:
        if num[hi] not in reversed_digits or num[lo] != reversed_digits[num[hi]]:
            return False

        lo += 1
        hi -= 1

    return True


class TestStrobogrammaticNumber(unittest.TestCase):
    def test_strobogrammatic_number(self):
        self.assertEqual(strobogrammatic_number("619"), True)
        self.assertEqual(strobogrammatic_number("68199866189"), True)
        self.assertEqual(strobogrammatic_number("9619196"), False)


if __name__ == "__main__":
    unittest.main()
