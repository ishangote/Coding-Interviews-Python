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


class TestAddStrings(unittest.TestCase):
    def test_add_strings(self):
        self.assertEqual(add_strings("99", "1"), "100")
        self.assertEqual(add_strings("11", "123"), "134")
        self.assertEqual(add_strings("456", "77"), "533")
        self.assertEqual(add_strings("0", "0"), "0")


if __name__ == "__main__":
    unittest.main()
