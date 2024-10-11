import unittest


def can_place_flowers(flower_bed, new_flowers):
    if new_flowers == 0:
        return True

    flower_bed = [0] + flower_bed + [0]

    for idx in range(1, len(flower_bed) - 1):
        if flower_bed[idx - 1] == flower_bed[idx] == flower_bed[idx + 1] == 0:
            new_flowers -= 1
            flower_bed[idx] = 1

            if new_flowers == 0:
                return True

    return False


class TestCanPlaceFlowers(unittest.TestCase):
    def test_can_place_flowers_edge(self):
        self.assertTrue(can_place_flowers([0], 1))
        self.assertTrue(can_place_flowers([1], 0))
        self.assertFalse(can_place_flowers([1], 1))

    def test_can_place_flowers(self):
        self.assertTrue(can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2))
        self.assertFalse(can_place_flowers([1, 0, 0, 1, 0, 1], 2))
        self.assertFalse(can_place_flowers([1, 0, 0, 0, 0, 1], 2))


if __name__ == "__main__":
    unittest.main()
