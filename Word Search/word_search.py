# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

"""
Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
              
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


SEE
^

"""

def word_search(board, word):
    if len(word) == 0: return True
    if len(board) == 0 or len(board[0]) == 0: return False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]: 
                if word_search_helper(board, word, i, j): return True
    
    return False