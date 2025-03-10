import unittest


# Time: O(4^n * n), where n => length of num
def expression_add_operators_eval(num, target):
    def backtrack(idx, expression):
        if idx == len(num) - 1:
            if eval(expression) == target:
                res.append(expression)
            return

        backtrack(idx + 1, f"{expression}+{num[idx + 1]}")
        backtrack(idx + 1, f"{expression}-{num[idx + 1]}")
        backtrack(idx + 1, f"{expression}*{num[idx + 1]}")

        if (idx == 0 and expression[0] == "0") or (
            idx > 0 and expression[-1] == "0" and expression[-2] in "+-*"
        ):
            return
        else:
            backtrack(idx + 1, f"{expression}{num[idx + 1]}")

    res = []
    backtrack(0, num[0])
    return res


# -------------------------------------------------------------------------------- #


# Time: O(4^n), where n => length of num
def expression_add_operators(num, target):
    def backtrack(idx, expression, total, prev_total):
        if idx == len(num):
            if total == target:
                res.append(expression)
            return
        else:
            for start in range(idx, len(num)):
                cur = int(num[idx : start + 1])
                if idx == 0:
                    backtrack(start + 1, f"{cur}", cur, 0)
                else:
                    backtrack(start + 1, f"{expression}+{cur}", total + cur, total)
                    backtrack(start + 1, f"{expression}-{cur}", total - cur, total)
                    backtrack(
                        start + 1,
                        f"{expression}*{cur}",
                        prev_total + (total - prev_total) * cur,
                        prev_total,
                    )
                if cur == 0:
                    return

    res = []
    backtrack(0, "", 0, 0)
    return res


class TestExpressionAddOperators(unittest.TestCase):
    def test_expression_add_operators_eval(self):
        self.assertListEqual(
            expression_add_operators_eval("123", 6), ["1+2+3", "1*2*3"]
        )
        self.assertListEqual(expression_add_operators_eval("123", -22), ["1-23"])
        self.assertListEqual(expression_add_operators_eval("05", 5), ["0+5"])
        self.assertListEqual(
            expression_add_operators_eval("105", 6), ["1+0+5", "1-0+5"]
        )
        self.assertListEqual(
            expression_add_operators_eval("232", 8), ["2+3*2", "2*3+2"]
        )

    def test_expression_add_operators(self):
        self.assertListEqual(expression_add_operators("123", 6), ["1+2+3", "1*2*3"])
        self.assertListEqual(expression_add_operators("123", -22), ["1-23"])
        self.assertListEqual(expression_add_operators("05", 5), ["0+5"])
        self.assertListEqual(expression_add_operators("105", 6), ["1+0+5", "1-0+5"])
        self.assertListEqual(expression_add_operators("232", 8), ["2+3*2", "2*3+2"])


if __name__ == "__main__":
    unittest.main()
