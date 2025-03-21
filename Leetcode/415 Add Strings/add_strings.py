import unittest


# Time: O(n + m), where n => length of num1, length of num2
# Space: O(1)
def add_strings(num1, num2):
    pt1, pt2 = len(num1) - 1, len(num2) - 1
    carry = 0
    res = []

    while pt1 >= 0 or pt2 >= 0:
        dig1 = int(num1[pt1]) if pt1 >= 0 else 0
        dig2 = int(num2[pt2]) if pt2 >= 0 else 0

        cur_sum = carry + dig1 + dig2

        res.append(str(cur_sum % 10))
        carry = cur_sum // 10

        pt1 -= 1
        pt2 -= 1

    if carry:
        res.append(str(carry))

    return "".join(res[::-1])


# --------------------------------------------------------------- #
# Variation 1: Decimal Points


def add_strings_helper(num1, num2, carry):
    pt1, pt2, carry = len(num1) - 1, len(num2) - 1, carry
    res = []

    while pt1 >= 0 or pt2 >= 0:
        dig1 = int(num1[pt1]) if pt1 >= 0 else 0
        dig2 = int(num2[pt2]) if pt2 >= 0 else 0

        cur_sum = dig1 + dig2 + carry
        res.append(str(cur_sum % 10))
        carry = cur_sum // 10

        pt1 -= 1
        pt2 -= 1

    if carry:
        res.append(str(carry))

    return "".join(res[::-1])


def add_strings_decimal_variation(num1, num2):
    (int1, frac1) = num1.split(".") if "." in num1 else (num1, "")
    (int2, frac2) = num2.split(".") if "." in num2 else (num2, "")

    if frac1 or frac2:
        max_frac_len = max(len(frac1), len(frac2))
        frac1 = frac1.ljust(max_frac_len, "0")
        frac2 = frac2.ljust(max_frac_len, "0")

        frac_sum = add_strings_helper(frac1, frac2, 0)

        carry = 0
        if len(frac_sum) > max_frac_len:
            carry = 1
            frac_sum = frac_sum[1:]

        int_sum = add_strings_helper(int1, int2, carry)

        return f"{int_sum}.{frac_sum}"

    return add_strings_helper(int1, int2, 0)


class TestAddStrings(unittest.TestCase):
    def test_add_strings(self):
        self.assertEqual(add_strings("99", "1"), "100")
        self.assertEqual(add_strings("11", "123"), "134")
        self.assertEqual(add_strings("456", "77"), "533")
        self.assertEqual(add_strings("0", "0"), "0")

    def test_add_strings_decimal_variation(self):
        self.assertEqual(add_strings_decimal_variation("91.465", "72.8"), "164.265")
        self.assertEqual(add_strings_decimal_variation(".15", "612"), "612.15")
        self.assertEqual(add_strings_decimal_variation("9.", "9.4"), "18.4")
        self.assertEqual(add_strings_decimal_variation("456", "77"), "533")


if __name__ == "__main__":
    unittest.main()
