import unittest


# Time: O(n), where n => length of expr
# Space: O(n)
def basic_calculator_ii(expr):
    expr = "".join(expr.split())

    last_sign, cur_num = "+", 0
    stack = []

    for idx, char in enumerate(expr):
        if char.isnumeric():
            cur_num = cur_num * 10 + int(char)

        if not char.isnumeric() or idx == len(expr) - 1:
            if last_sign == "+":
                stack.append(cur_num)

            elif last_sign == "-":
                stack.append(-1 * cur_num)

            elif last_sign == "*":
                stack.append(stack.pop() * cur_num)

            elif last_sign == "/":
                # Note: -3 // 2 = -2 and int(-3 / 2) = -1
                stack.append(int(stack.pop() / cur_num))

            else:
                pass

            last_sign = char
            cur_num = 0

    return sum(stack)


class TestBasicCalculatorII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(basic_calculator_ii(" 21 -4 * 3  +12"), 21)
        self.assertEqual(basic_calculator_ii("14-3/2"), 13)
        self.assertEqual(basic_calculator_ii("21-4*3*12"), -123)


if __name__ == "__main__":
    unittest.main()
