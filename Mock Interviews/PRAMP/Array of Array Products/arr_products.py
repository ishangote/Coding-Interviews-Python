"""
Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index 
(i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
"""

def array_of_array_products(arr):
    if not arr or len(arr) == 1 : return []
    prod = 1
    ans = []

    #Iteration 1: ->
    for i in range(len(arr)):
        ans.append(prod)
        prod *= arr[i]

    prod = 1

    #Iteration 2: <-
    for i in range(len(arr) - 1, -1, -1):
        ans[i] *= prod
        prod *= arr[i]

    return ans

import unittest
class TestArrayOfArrayProducts(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(array_of_array_products([]), [])
        self.assertEqual(array_of_array_products([1]), [])
    
    def test_generic(self):
        self.assertEqual(array_of_array_products([2, 2]), [2, 2])
        self.assertEqual(array_of_array_products([2, 7, 3, 4]), [84,24,56,42])
        self.assertEqual(array_of_array_products([2,3,0,982,10]), [0,0,58920,0,0])
        self.assertEqual(array_of_array_products([-3,17,430,-6,5,-12,-11,5]), [-144738000,25542000,1009800,-72369000,86842800,-36184500,-39474000,86842800])

if __name__ == "__main__": unittest.main()