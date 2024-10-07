import unittest


def self_dividing(num):
    cur_num = num

    while cur_num:
        digit = cur_num % 10
        if not digit or num % digit != 0:
            return False

        cur_num = cur_num // 10

    return True


# Time: O(n * d), where n => numbers in range and d => number of digits of largest number in range
# Space: O(1)
def self_dividing_numbers(left, right):
    res = []

    for itr in range(left, right + 1):
        if self_dividing(itr):
            res.append(itr)

    return res


class TestSelfDividing(unittest.TestCase):
    def test_self_dividing(self):
        self.assertEqual(
            self_dividing_numbers(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        )
        self.assertEqual(self_dividing_numbers(47, 85), [48, 55, 66, 77])


if __name__ == "__main__":
    unittest.main()
