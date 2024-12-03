import unittest


# Time: O(n), where n => number of digits in num
# Space: O(1), since only 10 digits exists
def maximum_swap(num):
    num_digits = list(str(num))
    last_occurrence = {int(digit): idx for idx, digit in enumerate(num_digits)}

    for idx, digit in enumerate(num_digits):
        for larger_digit in range(9, int(digit), -1):
            if larger_digit in last_occurrence and last_occurrence[larger_digit] > i:
                larger_idx = last_occurrence[larger_digit]

                num_digits[idx], num_digits[last_occurrence[larger_digit]] = (
                    num_digits[larger_idx],
                    num_digits[idx],
                )

                return int("".join(num_digits))

    return num


class TestMaximumSwap(unittest.TestCase):
    def test_maximum_swap(self):
        self.assertEqual(maximum_swap(2736), 7236)
        self.assertEqual(maximum_swap(9973), 9973)
        self.assertEqual(maximum_swap(9783), 9873)


if __name__ == "__main__":
    unittest.main()