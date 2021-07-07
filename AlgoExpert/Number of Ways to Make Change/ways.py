"""
Questions:
1. No way to make change? return 0
2. unlimited coins? yes

Examples:
n = 10
denoms = 
[1, 5, 10, 25]
       ^
ways = 
[1 1 1 1 1 2 2 2 2 2 4]
 0 1 2 3 4 5 6 7 8 9 10
                     i
					 
Time: O(d * n), d => number od denoms
Space: O(n)
"""

def number_of_ways(n, denoms):
    ways = [0] * (n + 1)
    ways[0] = 1

    for d in denoms:
        for idx in range(len(ways)):
            if idx < d: continue
            ways[idx] += ways[idx - d]
    
    return ways[-1]