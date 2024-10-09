import unittest


# Time: O(n), where n => length of input string
# Space: O(1)
def attendance_record(input_string):
    idx = 0
    absent_count = 0

    while idx < len(input_string):
        if input_string[idx] == "A":
            absent_count += 1
            if absent_count == 2:
                return False

            idx += 1

        elif input_string[idx] == "L":
            runner = idx

            while runner < len(input_string) and input_string[runner] == "L":
                runner += 1

            late_count = runner - idx

            if late_count >= 3:
                return False

            idx = runner

        else:
            idx += 1

    return True


class TestAttendanceRecord(unittest.TestCase):
    def test_attendance_record(self):
        self.assertTrue(attendance_record("PPALLP"))
        self.assertFalse(attendance_record("PPALLL"))


if __name__ == "__main__":
    unittest.main()
