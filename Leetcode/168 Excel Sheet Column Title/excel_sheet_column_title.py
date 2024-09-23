import unittest
import string


# Time: O(n), n => length of the output column title (reverse operation)
# Space: O(1)
def excel_sheet_column_title(column):
    character_map = {idx: letter for idx, letter in enumerate(string.ascii_uppercase)}

    res = []

    while column:
        last_character = character_map[(column - 1) % 26]
        res.append(last_character)
        column = (column - 1) // 26

    return "".join(res[::-1])


class TestExcelSheetColumnTitle(unittest.TestCase):
    def test_excel_sheet_column_title(self):
        self.assertEqual(excel_sheet_column_title(1), "A")
        self.assertEqual(excel_sheet_column_title(28), "AB")
        self.assertEqual(excel_sheet_column_title(701), "ZY")


if __name__ == "__main__":
    unittest.main()
