import unittest

# * Problem: Next Greater
# * Traversal Direction: Left to Right
# * Stack Type: Decreasing


# Time: O(n), where n => length of nums
# Space: O(n)
def next_greater_indices(nums):
    res = [-1] * len(nums)
    stack = []

    for idx in range(len(nums)):
        while stack and nums[idx] > nums[stack[-1]]:
            index = stack.pop()
            res[index] = idx

        stack.append(idx)

    return res


class TestNextGreaterIndices(unittest.TestCase):
    def test_next_greater_indices(self):
        self.assertListEqual(next_greater_indices([2, 1, 2, 4, 3]), [3, 2, 3, -1, -1])


if __name__ == "__main__":
    unittest.main()


"""
Input:
-> nums = 
 0  1  2  3  4
[2, 1, 2, 4, 3]

-> res =
  0   1   2   3   4
[-1, -1, -1, -1, -1]

-> stack = []

--------------------------------

-> nums = 
 0  1  2  3  4
[2, 1, 2, 4, 3]
 ^
-> res =
  0   1   2   3   4
[-1, -1, -1, -1, -1]

-> stack = [0]

--------------------------------

-> nums = 
 0  1  2  3  4
[2, 1, 2, 4, 3]
    ^
-> res =
  0   1   2   3   4
[-1, -1, -1, -1, -1]

-> stack = [0, 1]

--------------------------------

-> nums = 
 0  1  2  3  4
[2, 1, 2, 4, 3]
       ^
-> res =
  0   1   2   3   4             0   1   2   3   4
[-1, -1, -1, -1, -1]    =>    [-1,  2, -1, -1, -1]

-> stack = [0, 1] => [0]

--------------------------------

-> nums = 
 0  1  2  3  4
[2, 1, 2, 4, 3]
          ^
-> res =
  0   1   2   3   4
[-1,  2, -1, -1, -1]    =>     0   1   2   3   4
                              [3,  2, -1, -1, -1]

-> stack = [0]  => [3]
...

"""
