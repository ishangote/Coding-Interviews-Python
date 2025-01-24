import unittest


class MyCalendarBruteForce:
    def __init__(self):
        self.intervals = []

    def is_overlapping(self, current, given):
        return current[0] < given[1] and given[0] < current[1]

    # Time: O(n), where n => length of intervals
    def book_brute_force(self, start, end):
        for interval in self.intervals:
            if self.is_overlapping(interval, (start, end)):
                return False

        self.intervals.append((start, end))
        return True


# -------------------------------------------------------- #


class BTNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendarBST:
    def __init__(self):
        self.root = None

    # Time: O(logn), where n => number of intervals
    def insert_node(self, start, end):
        if not self.root:
            self.root = BTNode(start, end)
            return True

        cur = self.root

        while True:
            if end <= cur.start:
                if not cur.left:
                    cur.left = BTNode(start, end)
                    return True
                cur = cur.left
            elif start >= cur.end:
                if not cur.right:
                    cur.right = BTNode(start, end)
                    return True
                cur = cur.right
            else:
                return False

    def book(self, start, end):
        return self.insert_node(start, end)


class TestMyCalendar(unittest.TestCase):
    def test_my_calendar_brute_force(self):
        my_calendar = MyCalendarBruteForce()
        self.assertTrue(my_calendar.book_brute_force(10, 20))
        self.assertTrue(my_calendar.book_brute_force(5, 10))
        self.assertTrue(my_calendar.book_brute_force(20, 30))

        self.assertFalse(my_calendar.book_brute_force(15, 30))
        self.assertFalse(my_calendar.book_brute_force(5, 11))
        self.assertFalse(my_calendar.book_brute_force(12, 14))

    def test_my_calendar_bst(self):
        my_calendar = MyCalendarBST()
        self.assertTrue(my_calendar.book(10, 20))
        self.assertTrue(my_calendar.book(5, 10))
        self.assertTrue(my_calendar.book(20, 30))

        self.assertFalse(my_calendar.book(15, 30))
        self.assertFalse(my_calendar.book(5, 11))
        self.assertFalse(my_calendar.book(12, 14))


if __name__ == "__main__":
    unittest.main()
