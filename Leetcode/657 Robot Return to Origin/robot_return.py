from collections import Counter
import unittest


# Time: O(n), where n => length of moves
# Space: O(n)
def robot_return(moves):
    count_moves = Counter(moves)
    return count_moves["U"] == count_moves["D"] and count_moves["L"] == count_moves["R"]


class TestRobotReturn(unittest.TestCase):
    def test_robot_return(self):
        self.assertTrue(robot_return("UD"))
        self.assertFalse(robot_return("LL"))


if __name__ == "__main__":
    unittest.main()
