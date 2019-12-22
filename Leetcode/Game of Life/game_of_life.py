# According to the Wikipedia's article: "The Game of Life, also known simply as Life, 
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# Write a function to compute the next state (after one update) of the board given its current state. 
# The next state is created by applying the above rules simultaneously to every cell in the current state, 
# where births and deaths occur simultaneously.
# Could you solve it in-place? 
# Remember that the board needs to be updated at the same time: 
# You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. 
# In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. 
# How would you address these problems?
"""
i -> 0 1 2
j 
0    0 1 0
1    0 0 1
2    1 1 1
3    0 0 0

if live_count < 2 -> if curr == 1: curr = -1
                     if curr == 0: No change

if live_count == 2   if curr == 1: No change
                     if curr == 0: No change

if live_count == 3 -> if curr == 0: curr = 2
                      if curr == 1: No change

if live_count > 3 -> if curr == 1: curr = -1
                     if curr == 0: No change

neighbors = [(0, 1), (1, 0), (1, 1), (-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1)]

status = 2 => initially dead now alive
status = -1 => initially alive now dead

"""
def game_of_life(board):
    if not board or len(board) == 0: return None
    neighbors = [(0, 1), (1, 0), (1, 1), (-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1)]
    
    for row in range(len(board)):
        for col in range(len(board[0])):

            live_count = 0
            for neighbor in neighbors:
                r, c = row + neighbor[0], col + neighbor[1]
                if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                    #initially dead now alive
                    if board[r][c] == 1 or board[r][c] == -1:
                        live_count += 1
            
            if live_count < 2 and board[row][col] == 1:
                board[row][col] = -1
            
            elif live_count == 2 or live_count == 3:
                if live_count == 3 and board[row][col] == 0:
                    board[row][col] = 2

            else:
                if board[row][col] == 1:
                    board[row][col] = -1

    for row in range(len(board)):
        for col in range(len(board[0])):

            if board[row][col] <= 0: board[row][col] = 0
            else: board[row][col] = 1

    return board

import unittest
class TestGameOfLife(unittest.TestCase):
    def test_game_of_life_generic(self):
        board = [[0,1,0], [0,0,1], [1,1,1], [0,0,0]]
        self.assertEqual(game_of_life(board), [[0,0,0], [1,0,1], [0,1,1], [0,1,0]])

if __name__ == "__main__": unittest.main()