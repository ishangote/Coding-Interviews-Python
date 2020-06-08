"""
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all 
passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.
Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of 
your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Brute Force:
For each element in arr1 check all elements in arr2
O(n*m)

Case 1: n~m
Arrays are sorted
two pointer approach
i -> [0, n]
j -> [0, m]

Case 2: n >> m
Time Complexity: we running a binary search on arr2 N times. Hence the time complexity is O(N⋅log(M)). 
So why is this algorithm better than the previous one when M ≫ N? 
To demonstrate that let’s analyze the case that M = N^C, where C is a constant such that C. 
In this case, the time complexity of the second algorithm is: O(N⋅log(M)) = O(N⋅log(N^C)) = O(C⋅N⋅log(N)) = O(N⋅log(N)) 
And the time complexity of the first algorithm is: O(N + M) = O(N + N^C) = O(N^C) As we all know O(N^C) > O(N⋅log(N)).
"""

# len(arr1) ~ len(arr2)
# O(n + m)
def find_duplicates(arr1, arr2):
    ans, i, j = set(), 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]: 
            ans.add(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]: i += 1
        else: j += 1

    return ans

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target: return True
        if arr[mid] > target: hi = mid - 1
        else: lo = mid + 1
    return False

# len(arr1) >> len(arr2)
# n >> m
# O(mlog(n))
def find_duplicates_ii(arr1, arr2):
    ans = set()
    for num in arr2:
        if binary_search(arr1, num):
            ans.add(num)
    return ans

import unittest
class TestFindDuplicates(unittest.TestCase):
    def test_pramp(self):
        self.assertEqual(find_duplicates([1,3,5,9], [2,4,6,10]), set())
        self.assertEqual(find_duplicates([1,2,3,5,6,7], [3,6,7,8,20]), {3,6,7})
        self.assertEqual(find_duplicates([1,2,3,5,6,7], [7,8,9,10,11,12]), {7})

        self.assertEqual(find_duplicates_ii([1,3,5,9], [2,4,6,10]), set())
        self.assertEqual(find_duplicates_ii([1,2,3,5,6,7], [3,6,7,8,20]), {3,6,7})
        self.assertEqual(find_duplicates_ii([1,2,3,5,6,7], [7,8,9,10,11,12]), {7})

if __name__ == "__main__": unittest.main()
