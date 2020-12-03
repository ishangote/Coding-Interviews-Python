# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
"""
Questions:
1. Descending nums => profit negative? No 0
2. Are there duplicates in nums? Yes

Examples:
 0  1  2  3  4  5
[7, 1, 5, 3, 6, 4]

all pairs: (buy, sell)
(7, 1)
(7, 5)
(7, 3)
...
(1, 5)
(1, 3)
(1, 6) -> 5
...

Time: O(n^2)
Space: O(1)

---------------------------

 0  1  2  3  4  5
[7, 2, 5, 1, 6, 0]
                  ^
minimize buy, maximize sell
    
min_buy = 0
max_profit = 5

 0  1  2  3
[2, 5, 1, 3]
          i
min_buy = 1
max_profit = 3

Pseudo:
if nums[i] > min_buy:
    max_profit = max(max_profit, nums[i] - min_buy)
else:
    min_buy = nums[i]

Time: O(n)
Space: O(1)

"""
#Brute Force
def buy_sell_stock_naive(prices):
    ans = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > ans: ans = prices[j] - prices[i]
    
    return ans

import sys
def buy_sell_stock(prices):
    if len(prices) <= 1: return 0
    max_profit = 0
    min_buy = sys.maxsize
    
    for idx in range(len(prices)):
        if prices[idx] > min_buy:
            max_profit = max(max_profit, prices[idx] - min_buy)
        else:
            min_buy = prices[idx]
    
    return max_profit

if __name__ == "__main__":
    # number of elements 
    n = int(input("Enter number of stocks: ")) 
    # Below line read inputs from user using map() function  
    prices = list(map(int, input("Enter the prices for stocks : ").strip().split()))
    print("Max profit: " + str(buy_sell_stock(prices)))