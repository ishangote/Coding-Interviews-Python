"""
Questions:
1. is width == height? not necessary
2. go down or right
3. start top left end bottom right? yes

Examples:
m, n = 4, 3
   0 1 2 3
 0 1 1 1 1
 1 1 2 3 4
 2 1 3 6 10
 
 
m, n = 4, 5
  0 1 2  3 
0 1 1 1  1  
1 1 2 3  4
2 1 3 6  10
3 1 4 10 20
4 1 5 15 35
"""
# Time: O(w * h)
# Space: O(w * h)
def num_ways_naive(width, height):
    if width * height < 2: return 1
    ways = [[1 for i in range(width)] for j in range(height)]

    for i in range(1, len(ways)):
        for j in range(1, len(ways[0])):
            ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

    return ways[-1][-1]

# Time: O(w * h)
# Space: O(w)
def num_ways_space_optim(width, height):
    if width * height < 2: return 1
    
    prev = [1] * width
    cur = [1] * width

    for i in range(1, height):
        for idx in range(1, len(cur)):
            cur[idx] = cur[idx - 1] + prev[idx]
        
        prev = cur
    
    return cur[-1]

# Time: O(w + h)
# Space: O(1)
# formula = [(w - 1) + (h -1)]! // [(w - 1)! * (h - 1)!]

def factorial(n):
    if n == 0 or n == 1: return 1
    return n * factorial(n - 1)

def num_ways_time_optim(width, height):
    return factorial(width + height - 2) // (factorial(width - 1) * factorial(height - 1))