import unittest


# Time: O(n), where n => length of input_string
# Space: O(1)
def license_key_formatting(input_string, k):
    res = ""
    count = 0

    for idx in range(len(input_string) - 1, -1, -1):
        char = input_string[idx]

        if not char.isalnum():
            continue

        count += 1

        if count > k:
            res += f"-{char.upper()}"
            count = 1

        else:
            res += f"{char.upper()}"

    return res[::-1]


class TestLicenseKeyFormatting(unittest.TestCase):
    def test_license_key_formatting(self):
        self.assertEqual(license_key_formatting("5F3Z-2e-9-w", 2), "5F-3Z-2E-9W")


if __name__ == "__main__":
    unittest.main()
