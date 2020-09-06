# Given an array of 4 digits, return the largest 24 hour time that can be made.
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

"""
Example 1:
Input: A = [1,2,3,4]
Output: "23:41"

Example 2:
Input: A = [5,5,5,5]
Output: ""

Example 3:
Input: A = [0,0,0,0]
Output: "00:00"

Example 4:
Input: A = [0,0,1,0]
Output: "10:00"



"""
def permutations(arr):
    arr = sorted(arr)
    ans = []
    cur = []
    used_idx = [False] * len(arr)
    backtrack(ans, cur, used_idx, arr)
    return ans

def backtrack(ans, cur, used_idx, arr):
    if len(cur) == len(arr): ans.append(list(cur))

    else:
        for i in range(len(arr)):
            if used_idx[i] or (i > 0 and arr[i] == arr[i - 1] and not used_idx[i]):
                continue
            cur.append(arr[i])
            used_idx[i] = True
            backtrack(ans, cur, used_idx, arr)
            used_idx[i] = False
            cur.pop()
            
def largestTimeFromDigits(arr):
    arr_permut = permutations(arr)

    cur_time = -1
    ans = ''
    for h1, h2, m1, m2 in arr_permut:
        if 0 <= h1 * 10 + h2 < 24 and 0 <= m1 * 10 + m2 < 60 and (h1 * 10 + h2) * 60 + (m1 * 10 + m2) > cur_time:
            ans = str(h1) + str(h2) + ':' + str(m1) + str(m2)

    return ans

import unittest
class TestLargestTimeForGivenDigits(unittest.TestCase):
    def test_largest_time(self):
        self.assertEqual(largestTimeFromDigits([1, 2, 3, 4]), "23:41")
        self.assertEqual(largestTimeFromDigits([5, 5, 5, 5]), "")
        self.assertEqual(largestTimeFromDigits([0, 0, 0, 0]), "")

if __name__ == "__main__": unittest.main()