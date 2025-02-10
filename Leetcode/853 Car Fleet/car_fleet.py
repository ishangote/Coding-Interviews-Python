import unittest


# Time: O(nlogn), where n => number of cars
# Space: O(n)
def car_fleet(target, position, speed):
    position_speed = sorted([(pos, sp) for pos, sp in zip(position, speed)])
    stack = []

    for pos, sp in position_speed[::-1]:
        stack.append((target - pos) / sp)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


class TestCarFleet(unittest.TestCase):
    def test_car_fleet(self):
        self.assertEqual(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)
        self.assertEqual(car_fleet(10, [3], [3]), 1)
        self.assertEqual(car_fleet(100, [0, 2, 4], [4, 2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
