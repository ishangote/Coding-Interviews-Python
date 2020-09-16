"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

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

board = 
   0   1   2   3
0['A','B','C','E'],
1['S','F','C','S'],
2['A','D','E','E']

word = "ABCCED"
        012345

"""
def word_search_helper(board, word, i, j):
    if not word: return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]: return False
    tmp = board[i][j]
    board[i][j] = '#'
    return_flag = word_search_helper(board, word[1:], i + 1, j) or word_search_helper(board, word[1:], i - 1, j) or word_search_helper(board, word[1:], i, j + 1) or word_search_helper(board, word[1:], i, j - 1)
    board[i][j] = tmp
    return return_flag

def word_search(board, word):
    #Input Validations
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                if word_search_helper(board, word, row, col): return True
    return False

"""
board = 
   0   1   2   3
0['#','#','#','E'],
1['S','F','#','S'],
2['A','#','#','E']

word = "ABCCED"
        012345

tmp = A

"""