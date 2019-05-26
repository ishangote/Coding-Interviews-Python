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

def word_search_helper(board, word, row, col):
  if len(word) == 0: return True

  if 0 <= row < len(board) and 0 <= col < len(board[0]):
    if board[row][col] == word[0]:
      board[row][col] = '#'
      return word_search_helper(board, word[1:], row + 1, col) or word_search_helper(board, word[1:], row - 1, col) or word_search_helper(board, word[1:], row, col + 1) or word_search_helper(board, word[1:], row, col - 1)
    else: return False

  return False

import unittest
class TestWordSearch(unittest.TestCase):
  def test_invlaid_input(self):
    self.assertEqual(word_search([], "SEE"), False)
    self.assertEqual(word_search([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], ""), True)

  def test_word_search_word_found(self):
    self.assertEqual(word_search([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "SEE"), True)
    self.assertEqual(word_search([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "ABCCED"), True)

  def test_word_search_word_not_found(self):
    self.assertEqual(word_search([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "ABCB"), False)
    self.assertEqual(word_search([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "FEE"), False)

if __name__ == "__main__": unittest.main()