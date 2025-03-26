import unittest


# Time: O(n), where n => length of string
# Space: O(n)
def basic_calculator(input_string):
    if not input_string:
        return 0

    stack = []
    res, cur = 0, 0
    sign = 1

    for ch in input_string:
        if ch.isdigit():
            cur = cur * 10 + int(ch)

        elif ch == "+":
            res += sign * cur
            cur = 0
            sign = 1

        elif ch == "-":
            res += sign * cur
            cur = 0
            sign = -1

        elif ch == "(":
            stack.append(res)
            res = 0
            stack.append(sign)
            sign = 1

        elif ch == ")":
            res += sign * cur
            cur = 0
            prev_sign = stack.pop()
            prev_res = stack.pop()

            res = prev_res + prev_sign * res

        else:
            continue

    return res + sign * cur


class TestBasicCalculator(unittest.TestCase):
    def test_basic_calculator(self):
        self.assertEqual(basic_calculator(" 2-1 + 2 "), 3)
        self.assertEqual(basic_calculator("11-(2+3)-4"), 2)
        self.assertEqual(basic_calculator("(1+(4+5+2)-3)+(6+8)"), 23)
        self.assertEqual(basic_calculator("- (3 + (4 + 5))"), -12)
        self.assertEqual(basic_calculator("10 + (2 - 3) + 7"), 16)
        self.assertEqual(basic_calculator("1 - (2 - (3 - (4 - 5)))"), 3)


if __name__ == "__main__":
    unittest.main()
