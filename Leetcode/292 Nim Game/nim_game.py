import unittest


# Time: O(3^n)
# Space: O(n)
def recursive_helper(n, my_turn):
    if n == 0:
        return not my_turn

    if my_turn:
        for next_n in [n - 1, n - 2, n - 3]:
            if next_n >= 0 and recursive_helper(next_n, False):
                return True
        return False

    else:
        for next_n in [n - 1, n - 2, n - 3]:
            if next_n >= 0 and not recursive_helper(next_n, True):
                return False
        return True


def nim_game_brute_force(n):
    return recursive_helper(n, True)


# Time: O(1)
# Space: O(1)
def nim_game_optimized(n):
    return True if n % 4 != 0 else False


class TestNimGame(unittest.TestCase):
    def test_nim_game_brute_force(self):
        self.assertEqual(nim_game_brute_force(1), True)
        self.assertEqual(nim_game_brute_force(2), True)
        self.assertEqual(nim_game_brute_force(3), True)
        self.assertEqual(nim_game_brute_force(4), False)
        self.assertEqual(nim_game_brute_force(5), True)
        self.assertEqual(nim_game_brute_force(6), True)
        self.assertEqual(nim_game_brute_force(7), True)
        self.assertEqual(nim_game_brute_force(8), False)
        self.assertEqual(nim_game_brute_force(9), True)

    def test_nim_game_optimized(self):
        self.assertEqual(nim_game_optimized(1), True)
        self.assertEqual(nim_game_optimized(2), True)
        self.assertEqual(nim_game_optimized(3), True)
        self.assertEqual(nim_game_optimized(4), False)
        self.assertEqual(nim_game_optimized(5), True)
        self.assertEqual(nim_game_optimized(6), True)
        self.assertEqual(nim_game_optimized(7), True)
        self.assertEqual(nim_game_optimized(8), False)
        self.assertEqual(nim_game_optimized(9), True)


if __name__ == "__main__":
    unittest.main()
