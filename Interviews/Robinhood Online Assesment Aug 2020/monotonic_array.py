"""
For all sub-arrays of length 3 an array 
if subarr[i] > subarr[i + 1] > subarr[i + 2] or subarr[i] < subarr[i + 1] < subarr[i + 2]: ans[i] = 1 else 0


arr =
[1, 2, 1, -4, 5, 10]
ans =
[0, 1, 0, 1]

"""
def is_monotonic(arr):
    ans = []
    for i in range(len(arr) - 2):
        if (arr[i] > arr[i + 1] > arr[i + 2]) or (arr[i] < arr[i + 1] < arr[i + 2]): ans.append(1)
        else: ans.append(0)
    
    return ans

import unittest
class TestMonotonicArray(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(is_monotonic([1, 2, 1, -4, 5, 10]), [0, 1, 0, 1])
        self.assertEqual(is_monotonic([10, 10, 10, 10, 10]), [0, 0, 0])

if __name__ == "__main__": unittest.main()
     