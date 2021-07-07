"""
Questions:
1. if not possible to make change, return -1
2. Are denoms -ve? No
3. target = 0? return 0

Examples:
n = 7
denoms = [1, 5, 7]
		  ^
coins = 
[0 ~ ~ ~ ~ ~ ~ ~]
 0 1 2 3 4 5 6 7

coins = 
[0 1 2 3 4 1 2 3]
 0 1 2 3 4 5 6 7
               i
			   
Time: O(n * d)
Space: O(n)
"""
import sys
def min_coins(n, denoms):
    coins = [sys.maxsize] * (n + 1)
    coins[0] = 0

    for idx in range(len(coins)):
        for d in denoms:
            if idx < d: continue
            coins[idx] = min(coins[idx], 1 + coins[idx - d])
    
    return coins[-1] if coins[-1] != sys.maxsize else -1