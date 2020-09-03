# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and 
# empty spaces . The integer division should truncate toward zero.
"""
Example 1:
Input: "3+2*2"
Output: 7

Example 2:
Input: " 3/2 "
Output: 1

Example 3:
Input: " 3+5 / 2 "
Output: 5

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

012345678
21-4*3*12 
        ^

i   last_sign   curr_num    cur_sign    stack
init    +           0                   []
0       +           2                   []
1       +           21                  []
2       +           21         -        [21]
3       -           4                   [21]
4       -           4          *        [21, -4]
5       *           3                   [21, -4] 
6       *           3          *        [21, -12]
7       *           1                   [21, -12]
8       *           12                  [21, -144]


"""

def basic_calculator_ii(expr):
    expr = "".join(expr.split())
    last_sign, curr_num, stack = '+', 0, []
     
    for idx in range(len(expr)):
        if expr[idx].isnumeric(): 
            curr_num = curr_num * 10 + int(expr[idx])

        if not expr[idx].isnumeric() or idx == len(expr) - 1:
            curr_sign = expr[idx]
            if last_sign == "+":
                stack.append(curr_num)
            
            elif last_sign == "-":
                stack.append(-curr_num)

            elif last_sign == "*":
                stack.append(stack.pop() * curr_num)

            else:
                # NOTE -3 // 2 = -2 and int(-3 / 2) = -1
                stack.append(int(stack.pop() / curr_num))

            last_sign = curr_sign
            curr_num = 0

    return sum(stack)        
            
import unittest
class TestBasicCalculatorII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(basic_calculator_ii(" 21 -4 * 3  +12"), 21)
        self.assertEqual(basic_calculator_ii("14-3/2"), 13)

if __name__ == "__main__": unittest.main()