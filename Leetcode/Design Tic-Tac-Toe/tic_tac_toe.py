"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
"""

"""
board = 
    0   1   2
0   X       X

1       X

2   O   O   O

Maintain count of moves done by a player on each row, col, diag. If count == n: return player

rows = {
    p1: [0, 0, 0]
    p2: [0, 0, 0]
}

cols = {
    p1: [0, 0, 0]
    p2: [0, 0, 0]
}

diag = {
    p1:[0, 0]
    p2:[0, 0]
}

How to identify if (row, col) on diag or anti_diag or none?

board = 
    0   1   2
0   X       X

1       X

2   O   O   O

on diag = [(0, 0), (1, 1), (2, 2)]          => row - col = 0
on anti_diag = [(0, 2), (1, 1), (2, 0)]     => row + col = 2
none =  [(0, 1), (1, 0), (1, 2), (2, 1)]    => row - col, row + col neither

NOTE: n == 2:

    0   1
0
1

"""

class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = {"p1": [0] * self.n, "p2": [0] * self.n}
        self.cols = {"p1": [0] * self.n, "p2": [0] * self.n}
        self.diags = {"p1": [0, 0], "p2": [0, 0]}

    def move(self, row, col, player):
        p = "p1" if player == 1 else "p2"
        
        self.rows[p][row] += 1
        if self.rows[p][row] == self.n: return 1 if p == "p1" else 2
        
        self.cols[p][col] += 1
        if self.cols[p][col] == self.n: return 1 if p == "p1" else 2

        if row - col == 0:
            self.diags[p][0] += 1
            if self.diags[p][0] == self.n: return 1 if p == "p1" else 2

        if row + col == self.n - 1:
            self.diags[p][1] += 1
            if self.diags[p][1] == self.n: return 1 if p == "p1" else 2

        return 0

import unittest
class TestTicTacToe(unittest.TestCase):
    def test_tic_tac_toe_1(self):
        board = TicTacToe(3)
        self.assertEqual(board.move(0, 0, 1), 0)
        self.assertEqual(board.move(0, 2, 2), 0)
        self.assertEqual(board.move(2, 2, 1), 0)
        self.assertEqual(board.move(1, 1, 2), 0)
        self.assertEqual(board.move(2, 0, 1), 0)
        self.assertEqual(board.move(1, 0, 2), 0)
        self.assertEqual(board.move(2, 1, 1), 1)

    def test_tic_tac_toe_2(self):
        board = TicTacToe(2)
        self.assertEqual(board.move(0, 1, 1), 0)
        self.assertEqual(board.move(1, 1, 2), 0)
        self.assertEqual(board.move(1, 0, 1), 1)

    def test_tic_tac_toe_3(self):
        board = TicTacToe(3)
        self.assertEqual(board.move(1, 1, 2), 0)
        self.assertEqual(board.move(0, 2, 2), 0)
        self.assertEqual(board.move(2, 0, 2), 2)

if __name__ == "__main__": unittest.main()