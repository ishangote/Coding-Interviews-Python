"""
Questions:
1. The difference is absolute diff? yes
2. arr1/arr2 empty? no arrays are non empty 
3. Multiple solutions? No. Assume only one solution exists
4. Are the arrays sorted? No

Examples:
arr1 = 
[-1, 5, 10, 20, 28, 3]
arr2 =
[26, 134, 135, 15, 17]

Naive Approach:
Check all pairs
"""
import sys
import unittest
def smallest_difference_naive(arr1, arr2):
    assert(len(arr1) > 0 and len(arr2) > 0)
    min_diff = sys.maxsize
    ans = []
    for num1 in arr1:
        for num2 in arr2:
            if abs(num1 - num2) < min_diff:
                min_diff = abs(num1 - num2)
                ans = [num1, num2]
    return ans

"""
Time: O(n * m) n -> len)(arr1) and m -> len(arr2)
Space: O(1)
"""

"""
Examples:
arr1 = 
[-1, 5, 10, 20, 28, 3]
arr2 =
[26, 134, 135, 15, 17]

sort arr1
[-1, 3, 5, 10, 20, 28]
                      ^

sort arr2
[15, 17, 26, 134, 135]
             ^
abs diff = 2
ans = [26, 28]

"""
import sys
def smallest_difference_optim(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	
	min_diff = sys.maxsize
	i, j = 0, 0
	ans = []
	while i < len(arrayOne) and j < len(arrayTwo):
		diff = abs(arrayOne[i] - arrayTwo[j])
		if diff == 0: return [arrayOne[i], arrayTwo[j]]
		
		if diff < min_diff: 
			min_diff = diff
			ans = [arrayOne[i], arrayTwo[j]]
		
		if arrayOne[i] < arrayTwo[j]: i += 1
		else: j += 1
			
	return ans

"""
Time: O(n + m)
Space: O(1)
"""
class TestSmallestDifference(unittest.TestCase):
    algo_tests = []
    
    def setUp(self) -> None:
        self.algo_tests = [[[-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17], [28, 26]], [[-1, 5, 10, 20, 3], [26, 134, 135, 15, 17], [20, 17]], [[10, 1000], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530], [1000, 1014]], [[10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530], [530, 530]]]
        return super().setUp()

    def test_algo_expert_testcases(self):
        for test in self.algo_tests:
            arr1 = test[0]
            arr2 = test[1]
            expected_ans = test[2]
            self.assertEqual(expected_ans, smallest_difference_optim(arr1, arr2))

if __name__ == "__main__": unittest.main()