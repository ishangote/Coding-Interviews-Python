import unittest
from unittest.mock import MagicMock


class Robot:
    """
    This is the robot's control interface.
    You should not implement it, or speculate about its implementation
    """

    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        pass

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        pass


def move_left(robot: Robot):
    robot.turnLeft()
    can_move = robot.move()
    robot.turnRight()
    return can_move


def move_right(robot: Robot):
    robot.turnRight()
    can_move = robot.move()
    robot.turnLeft()
    return can_move


def move_up(robot: Robot):
    return robot.move()


def move_down(robot: Robot):
    robot.turnRight()
    robot.turnRight()
    can_move = robot.move()
    robot.turnRight()
    robot.turnRight()
    return can_move


def recursive_helper(robot, row, col, visited):
    robot.clean()
    visited.add((row, col))

    # Move Left
    if (row, col - 1) not in visited:
        can_move = move_left(robot)
        if not can_move:
            visited.add((row, col - 1))
        else:
            recursive_helper(robot, row, col - 1, visited)
            move_right(robot)

    # Right
    if (row, col + 1) not in visited:
        can_move = move_right(robot)
        if not can_move:
            visited.add((row, col + 1))
        else:
            recursive_helper(robot, row, col + 1, visited)
            move_left(robot)

    # Top
    if (row + 1, col) not in visited:
        can_move = move_up(robot)
        if not can_move:
            visited.add((row + 1, col))
        else:
            recursive_helper(robot, row + 1, col, visited)
            move_down(robot)

    # Bottom
    if (row - 1, col) not in visited:
        can_move = move_down(robot)
        if not can_move:
            visited.add((row - 1, col))
        else:
            recursive_helper(robot, row - 1, col, visited)
            move_up(robot)


# Time: O(n), where n => number of accessible cells.
# Space: O(n)
def clean_room(robot: Robot):
    recursive_helper(robot, 0, 0, set())


class TestRobotCleaning(unittest.TestCase):
    def setUp(self):
        # Create a mock robot instance
        self.robot = MagicMock()

        # Define a sample room layout
        # 1 - empty space, 0 - wall
        self.room = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]

        # Robot starts at (1,0), facing up
        self.start_pos = (1, 0)
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
        self.current_pos = self.start_pos
        self.current_dir = 0  # Facing up
        self.cleaned = set()

    def mock_move(self):
        dx, dy = self.directions[self.current_dir]
        new_x, new_y = self.current_pos[0] + dx, self.current_pos[1] + dy

        if (
            0 <= new_x < len(self.room)
            and 0 <= new_y < len(self.room[0])
            and self.room[new_x][new_y] == 1
        ):
            self.current_pos = (new_x, new_y)
            return True
        return False

    def mock_turn_left(self):
        self.current_dir = (self.current_dir - 1) % 4

    def mock_turn_right(self):
        self.current_dir = (self.current_dir + 1) % 4

    def mock_clean(self):
        self.cleaned.add(self.current_pos)

    def test_cleaning_algorithm(self):
        # Assign mocks to the robot API
        self.robot.move.side_effect = self.mock_move
        self.robot.turnLeft.side_effect = self.mock_turn_left
        self.robot.turnRight.side_effect = self.mock_turn_right
        self.robot.clean.side_effect = self.mock_clean

        clean_room(self.robot)

        # Expected cleaned cells (all reachable ones)
        expected_cleaned = {
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 0),
            (1, 3),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
        }

        self.assertEqual(self.cleaned, expected_cleaned)


if __name__ == "__main__":
    unittest.main()
