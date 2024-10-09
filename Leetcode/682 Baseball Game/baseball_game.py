from typing import Final
import unittest


# Time: O(n), where n => number of operations
# Space: O(n)
def baseball_game(operations):
    record = []

    INVALIDATE: Final[str] = "C"
    DOUBLE: Final[str] = "D"
    ADD: Final[str] = "+"

    for op in operations:
        # isdigit() returns False for negative numbers
        if op.strip("-").isdigit():
            record.append(int(op))

        elif op == INVALIDATE:
            record.pop()

        elif op == DOUBLE:
            if record:
                record.append(2 * record[-1])

        elif op == ADD:
            if len(record) >= 2:
                record.append(record[-1] + record[-2])

        else:
            pass

    return sum(record)


class TestBaseBallGame(unittest.TestCase):
    def test_baseball_game(self):
        self.assertEqual(baseball_game(["5", "2", "C", "D", "+"]), 30)
        self.assertEqual(baseball_game(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)
        self.assertEqual(baseball_game(["1", "C"]), 0)


if __name__ == "__main__":
    unittest.main()
