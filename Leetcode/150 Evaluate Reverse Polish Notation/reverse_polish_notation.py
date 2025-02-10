import unittest


# Time: O(n), where n => number of tokens
# Space: O(n)
def evaluate_rpn(tokens):
    stack = []

    for token in tokens:
        # To check if -ve integer string is number
        if token.strip("-").isdigit():
            stack.append(int(token))

        else:
            number2 = stack.pop()
            number1 = stack.pop()

            if token == "+":
                stack.append(number1 + number2)

            elif token == "-":
                stack.append(number1 - number2)

            elif token == "*":
                stack.append(number1 * number2)

            elif token == "/":
                # Truncate towards 0
                stack.append(int(number1 / number2))

    return stack[-1]


class TestEvaluateReversePolishNotation(unittest.TestCase):
    def test_evaluate_rpn(self):
        self.assertEqual(evaluate_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(evaluate_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(
            evaluate_rpn(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ),
            22,
        )


if __name__ == "__main__":
    unittest.main()
