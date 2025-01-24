import unittest


def recursive_helper(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "X":
        board[row][col] = "."

        recursive_helper(board, row, col + 1)
        recursive_helper(board, row + 1, col)

    return


# Time: O(n x m), where n => number of rows, m => number of cols
# Space: O(n x m), implied call stack memory
def battleships_in_board(board):
    res = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ".":
                continue

            res += 1
            recursive_helper(board, row, col)

    return res


class TestBattleshipsInBoard(unittest.TestCase):
    def test_battleships_in_board(self):
        board = [["X", ".", ".", "X"], ["X", ".", ".", "X"], [".", "X", ".", "X"]]
        self.assertEqual(battleships_in_board(board), 3)

        board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
        self.assertEqual(battleships_in_board(board), 2)

        board = [["."]]
        self.assertEqual(battleships_in_board(board), 0)


if __name__ == "__main__":
    unittest.main()
