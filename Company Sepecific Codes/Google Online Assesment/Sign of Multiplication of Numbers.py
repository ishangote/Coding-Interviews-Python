def solution(arr):
    if not arr: return None
    ans = 1
    for n in arr:
        if n == 0: return 0
        elif n < 0: ans *= -1
    return ans

import unittest
class TestQuestion(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(solution([]), None)
    def test_generic(self):
        self.assertEqual(solution([1, -2, -3, 5]), 1)
        self.assertEqual(solution([1, 2, 3, -5]), -1)
        self.assertEqual(solution([1, 0, 3, -5]), 0)

if __name__ == "__main__": unittest.main()
