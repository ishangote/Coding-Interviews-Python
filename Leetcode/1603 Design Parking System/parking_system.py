import unittest
from typing import Final


class ParkingSystem:
    def __init__(self, big, medium, small):
        self.CAR_TYPE_BIG: Final[int] = 1
        self.CAR_TYPE_MEDIUM: Final[int] = 2
        self.CAR_TYPE_SMALL: Final[int] = 3

        self.open_spaces = {
            self.CAR_TYPE_BIG: big,
            self.CAR_TYPE_MEDIUM: medium,
            self.CAR_TYPE_SMALL: small,
        }

    def add_car(self, car_type):
        if self.open_spaces[car_type] > 0:
            self.open_spaces[car_type] -= 1
            return True

        return False


class TestParkingSystem(unittest.TestCase):
    def test_parking_system(self):
        parking_system = ParkingSystem(1, 1, 0)

        self.assertTrue(parking_system.add_car(1))
        self.assertTrue(parking_system.add_car(2))
        self.assertFalse(parking_system.add_car(3))
        self.assertFalse(parking_system.add_car(1))


if __name__ == "__main__":
    unittest.main()
