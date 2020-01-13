# Given a nested list of integers, implement an iterator to flatten it.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

"""
Example 1:
Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

[1, [4, 5], [6, [2, 3]]]


stack =>
ans = []            ans =[1]                                        ans = [1, 4, 5]
1                                                   4               
[4,5]           =>      [4,5]               =>      5           =>                      => ...
[6, [2, 3]]             [6, [2,3]]                  [6, [2,3]]         [6, [2,3]]


"""
class NestedListIterator:
    def __init__(self, nested_list):
        self.stack = nested_list[::-1]

    def flatten_util(self, lst):
        for x in lst[::-1]:
            self.stack.append(x)

    def flatten_list(self):
        ans = []
        while self.stack:
            if type(self.stack[-1]) == int: 
                ans.append(self.stack.pop())
            else: 
                self.flatten_util(self.stack.pop())
        return ans
    
import unittest
class TestFlattenListIterator(unittest.TestCase):
    def test_generic(self):
        n = NestedListIterator([1, [4, 5, [2]], [6, [2, 3]]])
        self.assertEqual(n.flatten_list(), [1, 4, 5, 2, 6, 2, 3])

        n = NestedListIterator([[1,1],2,[1,1]])
        self.assertEqual(n.flatten_list(), [1,1,2,1,1])

        n = NestedListIterator([1,[4,[6]]])
        self.assertEqual(n.flatten_list(), [1,4,6])
        
if __name__ == "__main__": unittest.main()