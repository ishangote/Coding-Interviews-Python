import unittest


# Time: O(m), where m => number of logs
# Space: O(m)
def exclusive_time_of_functions(n, logs):
    res = [0] * n
    stack = []

    for log in logs:
        func_id, operation, timestamp = log.split(":")
        func_id, timestamp = int(func_id), int(timestamp)

        if operation == "start":
            stack.append([func_id, timestamp, 0])

        else:
            last_func_id, start_time, nested_time = stack.pop()
            res[last_func_id] += (timestamp - start_time + 1) - nested_time

            if stack:
                stack[-1][2] += timestamp - start_time + 1

    return res


class TestExclusiveTimeOfFunctions(unittest.TestCase):
    def test_exclusive_time_of_functions(self):
        self.assertListEqual(
            exclusive_time_of_functions(
                2,
                [
                    "0:start:0",
                    "1:start:2",
                    "0:start:4",
                    "0:end:5",
                    "0:start:6",
                    "0:end:7",
                    "1:end:8",
                    "0:end:10",
                ],
            ),
            [8, 3],
        )
        self.assertListEqual(
            exclusive_time_of_functions(
                2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
            ),
            [3, 4],
        )
        self.assertListEqual(
            exclusive_time_of_functions(
                1,
                [
                    "0:start:0",
                    "0:start:2",
                    "0:end:5",
                    "0:start:6",
                    "0:end:6",
                    "0:end:7",
                ],
            ),
            [8],
        )


if __name__ == "__main__":
    unittest.main()