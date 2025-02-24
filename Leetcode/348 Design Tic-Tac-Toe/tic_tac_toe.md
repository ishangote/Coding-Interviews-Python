# 348. Design Tic-Tac-Toe

## Problem Statement

> Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
>
> 1. A move is guaranteed to be valid and is placed on an empty block.
> 2. Once a winning condition is reached, no more moves are allowed.
> 3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
>
> Implement the `TicTacToe` class:
>
> - `TicTacToe(int n)` Initializes the object the size of the board n.
> - `int move(int row, int col, int player)` Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
>   - 0 if there is no winner after the move,
>   - 1 if player 1 is the winner after the move, or
>   - 2 if player 2 is the winner after the move.

> Constraints:
>
> - 2 <= n <= 100
> - player is 1 or 2.
> - 0 <= row, col < n
> - (row, col) are unique for each different call to move.
> - At most n2 calls will be made to move.

## Examples

Example 1:

```
Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
```

## Solution

Tracking Row Counts in Tic-Tac-Toe

1. Why Track Rows as Lists?

- Instead of storing the full board (n x n grid), we maintain a count of marks per row for each player.
- This allows us to check for a win in O(1) time instead of scanning the board.

2. How Does It Work?

- `self.rows = {"player1": [0] * n, "player2": [0] * n}` initializes counters for each row.
- When a player moves at (row, col), we increment `self.rows[player][row] += 1`
- If `self.rows[player][row] == n`, the player wins (full row completed).

Example (3x3 Board, Player 1 Moves in Row 1):

```
self.rows["player1"] = [0, 1, 0]  # First move
self.rows["player1"] = [0, 2, 0]  # Second move
self.rows["player1"] = [0, 3, 0]  # Third move → Player 1 wins!
```

3. How to determine which diagonal the (row, col) belongs to?

```
if row - col == 0:
    diagonal
if row + col == n:
    anti-diagonal
```
