"""
[2, 6, 8, 9] k = 2

S1: [9, 8, 6, 2]
S2: [8, 9, 6, 2]
S3: [8, 9, 2, 6]

[2, 3, 7, 1, 5] k = 3
S1: [5, 1, 7, 3, 2]
S2: [7, 1, 5, 3, 2]
S3: [7, 1, 5, 2, 3]
"""

import unittest
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr

def rotate(arr, k):
    if len(arr) == 0: return []
    k %= len(arr)   #for cases arr = [2], k = 4
    arr = reverse(arr, 0, len(arr) - 1)
    arr = reverse(arr, 0, k - 1)
    arr = reverse(arr, k, len(arr) - 1)
    return arr

class TestRotateArray(unittest.TestCase):
    def test_empty_arr(self):
        self.assertEqual(rotate([], 3), [])

    def test_one_element(self):
        self.assertEqual(rotate([3], 4), [3])

    def test_even_length_arr(self):
        self.assertEqual(rotate([1, 2, 3, 4], 2), [3, 4, 1, 2])

    def test_odd_length_arr(self):
        self.assertEqual(rotate([3, 5, 1, 4, 8], 2), [4, 8, 3, 5, 1])

if __name__ == "__main__": unittest.main()
