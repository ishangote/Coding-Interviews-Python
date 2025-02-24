import unittest


class TicTacToe:
    # Space: O(n + n + 2) ~ O(n)
    def __init__(self, n):
        self.n = n
        # Each index represents a row, and the value at that index counts how many marks that player has in that row/col/diagonal
        self.rows = {1: [0] * self.n, 2: [0] * self.n}
        self.cols = {1: [0] * self.n, 2: [0] * self.n}
        self.diags = {1: [0, 0], 2: [0, 0]}

    # Time: O(1)
    def move(self, row, col, player):
        self.rows[player][row] += 1
        if self.rows[player][row] == self.n:
            return 1 if player == 1 else 2

        self.cols[player][col] += 1
        if self.cols[player][col] == self.n:
            return 1 if player == 1 else 2

        if row - col == 0:
            self.diags[player][0] += 1
            if self.diags[player][0] == self.n:
                return 1 if player == 1 else 2

        if row + col == self.n - 1:
            self.diags[player][1] += 1
            if self.diags[player][1] == self.n:
                return 1 if player == 1 else 2

        return 0


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

    def test_tic_tac_toe_3(self):
        board = TicTacToe(2)
        self.assertEqual(board.move(0, 1, 1), 0)
        self.assertEqual(board.move(1, 1, 2), 0)
        self.assertEqual(board.move(1, 0, 1), 1)


if __name__ == "__main__":
    unittest.main()
