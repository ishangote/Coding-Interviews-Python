# 489. Robot Room Cleaner

## Problem Statement

> You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.
>
> The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.
>
> You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.
>
> When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.
>
> Design an algorithm to clean the entire room using the following APIs:

```
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
 ` void clean()`;
}
```

> Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.
>
> Custom testing:
> The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.

## Examples

Example 1:

```
Input: room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
Output: Robot cleaned all rooms.
Explanation: All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
```

Example 2:

```
Input: room = [[1]], row = 0, col = 0
Output: Robot cleaned all rooms.
```

## Solution

The solution uses a recursive depth-first search (DFS) strategy to systematically explore and clean the entire room without knowing its layout beforehand. Below is an explanation of each part of the approach:

1. Movement Helper Functions

- `move_left(robot)`:

  - Action: Turns the robot left, attempts to move, and then turns it back right to restore the original orientation.
  - Purpose: This simulates a leftward move while ensuring that subsequent operations are relative to the same facing direction.

- `move_right(robot)`:

  - Action: Turns the robot right, attempts to move, and then turns it back left.
  - Purpose: This function allows the robot to move to the right and then maintain its original orientation.

- `move_up(robot)`:

  - Action: Since the robot starts facing up, calling move() directly attempts to move upward.
  - Purpose: It uses the robot’s natural forward direction as the "up" direction.

- `move_down(robot)`:
  - Action: Turns the robot 180 degrees (by turning right twice), attempts to move (which is equivalent to moving down), and then turns 180 degrees again to face the original direction.
  - Purpose: This function simulates a downward move while preserving the robot’s overall orientation.

2. Recursive Cleaning Strategy (DFS)

- Starting Point:
  The robot begins at an assumed coordinate (0, 0) and cleans the cell.

- Marking Visited Cells:
  A set called visited keeps track of all cells that have been cleaned or confirmed as obstacles (walls). This prevents the robot from re-entering the same cell or repeatedly trying to move into walls.

- Exploration Process:
  For each cell, the algorithm:

  1. Cleans the Current Cell: Calls `robot.clean()` to clean the cell.

  2. Attempts to Move in All Four Directions:
     - Left: If the left cell hasn’t been visited, the robot calls `move_left()`.
       - If it can move, it recursively explores that cell.
       - After exploration, it backtracks by moving right (using `move_right()`) to return to the original cell.
     - Right: Similarly, attempts to move right using `move_right()`, explores recursively if possible, and backtracks using `move_left()`.
     - Up: The robot moves forward (up) if the cell hasn’t been visited, explores, then backtracks by moving down (`move_down()`).
     - Down: The robot moves down using `move_down()`, explores recursively, and backtracks by moving up (`move_up()`).

3. Handling Obstacles:
   - If the robot cannot move in a direction (i.e., it hits a wall), that direction is marked as visited so that it isn’t attempted again.

- Backtracking:
  After exploring in any direction, the robot returns to the previous cell. This ensures that all paths are fully explored and the robot can eventually cover every reachable cell.

1. Overall Cleaning Routine

- `clean_room(robot)`:
  - Action: This is the main function that initiates the recursive DFS from the starting cell (0, 0).
  - Purpose: It ensures that the robot starts the cleaning process and continues until every accessible cell has been visited and cleaned.
