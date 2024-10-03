import unittest


# Time: O(nlogn + mlogm), where n => length of greeds m => length of cookies
# Space: O(1)
def assign_cookies(greeds, cookies):
    res = 0
    g_idx, c_idx = 0, 0

    greeds.sort()
    cookies.sort()

    while g_idx < len(greeds) and c_idx < len(cookies):
        if greeds[g_idx] <= cookies[c_idx]:
            res += 1
            g_idx += 1

        c_idx += 1

    return res


class TestAssignCookies(unittest.TestCase):
    def test_assign_cookies(self):
        self.assertEqual(assign_cookies([1, 2, 1, 3], [1, 3, 2]), 3)
        self.assertEqual(assign_cookies([10, 9, 8, 7], [5, 6, 7, 8]), 2)


if __name__ == "__main__":
    unittest.main()
