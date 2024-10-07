import unittest


# Time: O(log7n)
# Space: O(1)
def convert_to_base_7(num):
    res = "" if num else "0"
    abs_num = abs(num)

    while abs_num:
        res += str(abs_num % 7)
        abs_num //= 7

    return res[::-1] if num >= 0 else "-" + res[::-1]


class TestConvertToBase7(unittest.TestCase):
    def test_convert_to_base7(self):
        self.assertEqual(convert_to_base_7(0), "0")
        self.assertEqual(convert_to_base_7(100), "202")
        self.assertEqual(convert_to_base_7(-7), "-10")


if __name__ == "__main__":
    unittest.main()
