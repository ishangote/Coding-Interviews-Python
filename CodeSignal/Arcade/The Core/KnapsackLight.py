"""
You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?
Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

Example
For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
knapsackLight(value1, weight1, value2, weight2, maxW) = 10.
You can only carry the first item.

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
knapsackLight(value1, weight1, value2, weight2, maxW) = 16.
You're strong enough to take both of the items with you.

For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
knapsackLight(value1, weight1, value2, weight2, maxW) = 7.
"""
"""
Questions:
1. Is it 0/1 knapsack? -> Yes, we can not split the items
2. Are there negative weights, values? -> No

Example:
v1 = 10, w1 = 5
v2 = 6, w2 = 4
mw = 8

                   8
            3(10)       4(6)
         -2  -1       -1  0(12)* Can not use the second weight twice!

"""
import sys
def knapsackLight(value1, weight1, value2, weight2, maxW):
    def knapsack_util(cur_wt, cur_val, weight1, weight2):
        val1, val2 = 0, 0
        if cur_wt >= weight1:
            val1 = knapsack_util(cur_wt - weight1, cur_val + value1, sys.maxsize, weight2)
            
        if cur_wt >= weight2:
            val2 = knapsack_util(cur_wt - weight2, cur_val + value2, weight1, sys.maxsize)
        
        return max(val1, val2, cur_val)
        
    return knapsack_util(maxW, 0, weight1, weight2)