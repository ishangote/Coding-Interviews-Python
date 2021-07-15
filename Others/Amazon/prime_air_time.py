"""
arr1 = {{1, 2000}, {2, 3000}, {3, 4000} }
            j
arr2 = {{2, 3000}, {1, 5000 }}
                      i
x = 5000

target = 20
arr1 = [[1, 8], [2, 7], [3, 14]], 
           i
arr2 = [[1, 5], [2, 10], [3, 14]]
                            j
}

example: maxTravelDist = 10000
forwardRouteList[] = 
   0        1       2          3
[[1,3000],[2,5000],[3,7000],[4,10000]]
                    i
returnRouteList[] = 
[[1,2000],[2,3000],[3,4000],[4,5000]]
j

dist = 0
cur = [2, 4] 

res [[2, 4]]

O/p: [[2,4],[3,2]]
{
    2000: [[1, 4]]
    0: [[2, 4], [3, 2]]
    1000: [[3, 1]]
}

"""
import sys
from collections import defaultdict
def func(arr1, arr2, target):
    ans = []
    arr1.sort(key = lambda x: x[1])
    arr2.sort(key = lambda x: x[1])
    
    hm = defaultdict(list)
    
    min_diff = sys.maxsize

    i, j = 0, len(arr2) - 1
    while i < len(arr1) and j >= 0:
        cur = [arr1[i][0], arr2[j][0]]
        cur_diff = target - (arr1[i][1] + arr2[j][1])

        if cur_diff >= 0: 
            hm[cur_diff].append(cur)
            if arr1[i][1] <= arr2[j][1]: i += 1
            else: j -= 1
        else:
            j -= 1

    min_diff_item = sys.maxsize
    for k in hm:
        if min_diff_item > k: min_diff_item = k
    
    return hm[min_diff_item] if min_diff_item != sys.maxsize else []

import unittest
class TestMinDist(unittest.TestCase):
    def test_generic(self):
        self.assertEqual([[2,4],[3,2]], func([[1,3000],[2,5000],[3,7000],[4,10000]], [[1,2000],[2,3000],[3,4000],[4,5000]], 10000))
        self.assertEqual([], func([[1,3000],[2,5000],[3,10000],[4,10000]], [[1,10000],[2,10000],[3,10000],[4,10000]], 10000))
        self.assertEqual([[3, 1]], func([[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]], 20))

if __name__ == "__main__": unittest.main()