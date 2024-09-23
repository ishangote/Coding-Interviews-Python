import unittest
import string


# Time: O(n), where n => length of column_title
# Space: O(1), only store 26 character map
def excel_sheet_column_number(column_title):
    character_map = {
        letter: idx + 1 for idx, letter in enumerate(string.ascii_uppercase)
    }

    position, res = 0, 0

    for idx in range(len(column_title) - 1, -1, -1):
        res += character_map[column_title[idx]] * (26**position)
        position += 1

    return res


class TestExcelSheetColumnNumber(unittest.TestCase):
    def test_excel_sheet_column_number(self):
        self.assertEqual(excel_sheet_column_number("A"), 1)
        self.assertEqual(excel_sheet_column_number("AB"), 28)
        self.assertEqual(excel_sheet_column_number("ZY"), 701)


if __name__ == "__main__":
    unittest.main()
