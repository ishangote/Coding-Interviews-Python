import unittest


def is_valid_integer(s):
    """Checks if the given string represents a valid integer (with optional leading + or -)."""
    if not s:
        return False
    idx = 0

    # Allow optional leading sign
    if s[0] in "+-":
        idx += 1

    # The remaining part must contain only digits and must not be empty
    return idx < len(s) and s[idx:].isdigit()


def valid_number(s):
    """Checks if the given string represents a valid number, including decimals and scientific notation."""
    if not s:
        return False

    seen_digit = False  # At least one digit should be present
    seen_decimal = False  # Only one decimal point is allowed

    idx = 0

    # Allow optional leading sign
    if s[0] in "+-":
        idx += 1

    while idx < len(s):
        ch = s[idx]

        if ch.isdigit():
            seen_digit = True

        elif ch == ".":
            # A second decimal point makes it invalid
            if seen_decimal:
                return False
            seen_decimal = True

        elif ch in "Ee":
            # 'E' or 'e' must follow at least one digit and should be followed by a valid integer
            return seen_digit and is_valid_integer(s[idx + 1 :])

        else:
            # Any other character is invalid
            return False

        idx += 1

    return seen_digit  # Ensure at least one digit exists


class TestValidNumber(unittest.TestCase):
    def test_valid_number(self):
        self.assertTrue(valid_number("123"))
        self.assertTrue(valid_number("+123"))
        self.assertTrue(valid_number("-123"))
        self.assertTrue(valid_number("0"))
        self.assertTrue(valid_number("3.14"))
        self.assertTrue(valid_number("-3.14"))
        self.assertTrue(valid_number("+3.14"))
        self.assertTrue(valid_number("2e10"))
        self.assertTrue(valid_number("-2E10"))
        self.assertTrue(valid_number("3.14e2"))

        self.assertFalse(valid_number("abc"))
        self.assertFalse(valid_number("3.14.15"))
        self.assertFalse(valid_number("e3"))
        self.assertFalse(valid_number("3e"))
        self.assertFalse(valid_number("3e1.2"))
        self.assertFalse(valid_number("+-3"))
        self.assertFalse(valid_number("3e+"))
        self.assertFalse(valid_number("3e-"))


if __name__ == "__main__":
    unittest.main()
