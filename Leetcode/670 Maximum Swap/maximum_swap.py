import unittest


# Time: O(n), where n => number of digits in num
# Space: O(n)
def maximum_swap_two_pass(num):
    digits = list(str(num))
    n = len(digits)
    right_max = [0] * n

    right_max[-1] = n - 1
    for idx in range(n - 2, -1, -1):
        if digits[idx] > digits[right_max[idx + 1]]:
            right_max[idx] = idx  # If current digit is larger, store its own index
        else:
            right_max[idx] = right_max[idx + 1]  # Otherwise, inherit max index

    for idx in range(n):
        if digits[idx] < digits[right_max[idx]]:
            swap_idx = right_max[idx]
            digits[idx], digits[swap_idx] = digits[swap_idx], digits[idx]
            break

    return int("".join(digits))


# Time: O(n), where n => number of digits in num
# Space: O(1), since only 10 digits exists
def maximum_swap_one_pass(num):
    num_digits = list(str(num))
    last_occurrence = {int(digit): idx for idx, digit in enumerate(num_digits)}

    for idx, digit in enumerate(num_digits):
        for larger_digit in range(9, int(digit), -1):
            if larger_digit in last_occurrence and last_occurrence[larger_digit] > idx:
                larger_idx = last_occurrence[larger_digit]

                num_digits[idx], num_digits[larger_idx] = (
                    num_digits[larger_idx],
                    num_digits[idx],
                )

                return int("".join(num_digits))

    return num


class TestMaximumSwap(unittest.TestCase):
    def test_maximum_swap_two_pass(self):
        self.assertEqual(maximum_swap_two_pass(2736), 7236)
        self.assertEqual(maximum_swap_two_pass(9973), 9973)
        self.assertEqual(maximum_swap_two_pass(9783), 9873)

    def test_maximum_swap_one_pass(self):
        self.assertEqual(maximum_swap_one_pass(2736), 7236)
        self.assertEqual(maximum_swap_one_pass(9973), 9973)
        self.assertEqual(maximum_swap_one_pass(9783), 9873)


if __name__ == "__main__":
    unittest.main()
