import unittest
import string


def generate_sequential_digit_numbers(digits):
    for first_digit in range(1, 9):
        num, prev = first_digit, first_digit

        for itr in range(digits - 1):
            if prev == 9:
                return

            num = num * 10 + (prev + 1)
            prev += 1

        yield num

    return


# Time: O(1)
# Space: O(1)
def sequential_digits_generate_numbers(lo, hi):
    lo_digits, hi_digits = len(str(lo)), len(str(hi))
    res = []

    for digits in range(lo_digits, hi_digits + 1):
        for num in generate_sequential_digit_numbers(digits):
            if lo <= num <= hi:
                res.append(num)

    return res


# ------------------------------------------------- #


def generate_sequential_digit_substring(length):
    DIGITS = string.digits[1:]

    for idx in range(len(DIGITS) - length + 1):
        yield DIGITS[idx : idx + length]

    return


# Time: O(1)
# Space: O(1)
def sequential_digits_generate_substrings(lo, hi):
    lo_digits, hi_digits = len(str(lo)), len(str(hi))
    res = []

    for digits in range(lo_digits, hi_digits + 1):
        for substring in generate_sequential_digit_substring(digits):
            num = int(substring)
            if lo <= num <= hi:
                res.append(num)

    return res


class TestSequentialDigits(unittest.TestCase):
    def test_sequential_digits_generate_numbers(self):
        self.assertEqual(
            sequential_digits_generate_numbers(1000, 13000),
            [1234, 2345, 3456, 4567, 5678, 6789, 12345],
        )

    def test_sequential_digits_generate_substrings(self):
        self.assertEqual(
            sequential_digits_generate_substrings(1000, 13000),
            [1234, 2345, 3456, 4567, 5678, 6789, 12345],
        )


if __name__ == "__main__":
    unittest.main()
