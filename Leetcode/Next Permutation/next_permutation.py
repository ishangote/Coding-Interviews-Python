# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
"""
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
def nextPermutation(n):
    """
    Do not return anything, modify nums in-place instead.
    """
    idx = len(n) - 1
    
    while idx > 0 and n[idx - 1] >= n[idx]:
        idx -= 1

    if idx == 0:
        reverse(n, 0, len(n) - 1)
        return n

    pivot = idx - 1
        
    idx = len(n) - 1
    while n[idx] <= n[pivot]:
        idx -= 1
        
    swap(n, pivot, idx)
    reverse(n, pivot + 1, len(n) - 1)

    return n

def reverse(n, i, j):
    while i < j:
        swap(n, i, j)
        i += 1
        j -= 1

def swap(n, i, j):
    n[i], n[j] = n[j], n[i]

import unittest
class TestNextPermutation(unittest.TestCase):
    def test_next_permutation(self):
        self.assertEqual(nextPermutation([2, 1]), [1, 2])
        self.assertEqual(nextPermutation([2, 1, 3]), [2, 3, 1])

if __name__ == "__main__": unittest.main()