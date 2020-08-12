# Time  = O(1)
# Space = O(1)
def findLegalMoves(board, position):
    #Input Validations
    
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ans = []
    for d in dirs:
        nbr_x, nbr_y = d[0] + position[0], d[1] + position[1]
        if 0 <= nbr_x < len(board) and 0 <= nbr_y < len(board[0]) and board[nbr_x][nbr_y] != -1:
            ans.append((nbr_x, nbr_y))
            
    return ans

# Time = O(n)
# Space = O(n)
from collections import deque
def isReachable(board, end):
    #input validations
    
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0: count += 1
    
    queue = deque([end])
    visited = set()
    
    while queue:
        cur = queue.pop()
        visited.add(cur)
        nbrs = findLegalMoves(board, cur)
        
        for nbr in nbrs:
            if nbr not in visited: queue.appendleft(nbr)
        
    return len(visited) == count

"""
2x2 grid with contents => 0, -1, 1 where 1 is a treasure. Return a path which is shortest and covers ALL treasures.

Discussion:
This is an NP Hard problem. (Travelling Salesman Problem)
"""

'''
Feedback for Fellow
1. Don't cover your mouth with your hand while you're talking I know it's force of habit and you're thinking, but it muffles your voice and should be avoided
2. Good work taking hints and identifying the solution to the problem. Being able to pivot and abandon ideas that your interviewer doesn't like quickly is a great skill to have!
3. I had to ask you for time complexity for every variation to the problem, but you should be telling it to me. Remember, if you don't say it explicitly your interviewer may assume you're not familiar with the concepts!
4. The BFS took a little longer to code than I would have liked. This should be under 5-7 min if you're targeting a FAANG company.
5. Jumped into solutions too fast for the third problem without solving the problem by hand and verifying your algorithm works.
6. Remember competitive programming is different than coding interviews, your code quality is being judged too. Use good naming conventions and generally avoid writing code you wouldn't be ok with adding to a production repo.
7. Great work and good interview! You need more in-person help, but your algorithm skills are pretty solid!

Communication = 4/5
Problem-Solving = 4/5
Syntax = 3/5
Verification = 4/5
Total: 15/20
'''