"""
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


                                    ""
                    1__           2__           3__
                12_     13_     21_     23_     31_     32_
                123     132     213     231     312     323

"""

def permutations(nums):
    # nums = sorted(nums)
    ans = []
    cur = []
    backtrack(ans, cur, nums)
    return ans

def backtrack(ans, cur, nums):
    if len(cur) == len(nums):
        ans.append(list(cur))

    else:
        for i in range(len(nums)):
            if nums[i] in cur: continue
            cur.append(nums[i])
            backtrack(ans, cur, nums)
            cur.pop()
        
import unittest
class TestPermutations(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(permutations([1, 2, 3]), [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]])

if __name__ == "__main__": unittest.main()