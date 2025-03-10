import unittest


def minimum_remove_valid_parentheses(input_string):
    balance = 0
    open_remove, close_remove = 0, 0

    for ch in input_string:
        if ch == "(":
            balance += 1
        elif ch == ")":
            if balance == 0:
                close_remove += 1
            else:
                balance -= 1

    open_remove += balance

    return (open_remove, close_remove)


def recursive_helper(
    idx, balance, open_remove, close_remove, cur, res, memo, input_string
):
    state = (idx, balance, open_remove, close_remove, tuple(cur))
    if state in memo:
        return

    if idx == len(input_string):
        if balance == 0 and open_remove == 0 and close_remove == 0:
            res.add("".join(cur))
        return

    ch = input_string[idx]

    if ch not in "()":
        cur.append(ch)
        recursive_helper(
            idx + 1,
            balance,
            open_remove,
            close_remove,
            cur,
            res,
            memo,
            input_string,
        )
        cur.pop()

    else:
        if ch == "(":
            # Option 1: Remove the current '(' if possible.
            if open_remove > 0:
                recursive_helper(
                    idx + 1,
                    balance,
                    open_remove - 1,
                    close_remove,
                    cur,
                    res,
                    memo,
                    input_string,
                )
            # Option 2: Keep the '('.
            cur.append(ch)
            recursive_helper(
                idx + 1,
                balance + 1,
                open_remove,
                close_remove,
                cur,
                res,
                memo,
                input_string,
            )
            cur.pop()

        if ch == ")":
            if close_remove > 0:
                # Option 1: Remove the current ')' if possible.
                recursive_helper(
                    idx + 1,
                    balance,
                    open_remove,
                    close_remove - 1,
                    cur,
                    res,
                    memo,
                    input_string,
                )

            # Option 2: Keep the ')', only if there is a matching '(' (i.e. balance > 0).
            if balance > 0:
                cur.append(ch)
                recursive_helper(
                    idx + 1,
                    balance - 1,
                    open_remove,
                    close_remove,
                    cur,
                    res,
                    memo,
                    input_string,
                )
                cur.pop()


# Time: O(2^n), where n => length of input string
# Space: O(2^n), recursive call stack
def remove_invalid_parentheses(input_string):
    res = set()
    open_remove, close_remove = minimum_remove_valid_parentheses(input_string)

    recursive_helper(0, 0, open_remove, close_remove, [], res, set(), input_string)
    return list(res)


class TestRemoveInvalidParentheses(unittest.TestCase):
    def test_remove_invalid_parentheses(self):
        self.assertListEqual(
            remove_invalid_parentheses("()())()"), ["(())()", "()()()"]
        )
        self.assertListEqual(
            remove_invalid_parentheses("(a)())()"), ["(a())()", "(a)()()"]
        )
        self.assertListEqual(remove_invalid_parentheses(")("), [""])
        pass


if __name__ == "__main__":
    unittest.main()
