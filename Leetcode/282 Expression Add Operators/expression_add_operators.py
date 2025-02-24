import unittest


# FIXME: Code not working
def expression_add_operators(num, target):
    def backtrack(cur_expr, cur_total, idx, res):
        if idx == len(num):
            if cur_total == target:
                res.append(cur_expr)
            return

        backtrack(cur_expr + num[idx], cur_total, idx + 1, res)
        backtrack(cur_expr + "+" + num[idx], cur_total + int(num[idx]), idx + 1, res)
        backtrack(cur_expr + "-" + num[idx], cur_total - int(num[idx]), idx + 1, res)
        backtrack(cur_expr + "*" + num[idx], cur_total * int(num[idx]), idx + 1, res)

    res = []
    backtrack(num[0], int(num[0]), 1, res)
    return res


class TestExpressionAddOperators(unittest.TestCase):
    def test_expression_add_operators(self):
        self.assertListEqual(expression_add_operators("123", 6), ["1+2+3", "1*2*3"])
        self.assertListEqual(expression_add_operators("232", 8), ["2*3+2", "2+3*2"])


if __name__ == "__main__":
    unittest.main()
