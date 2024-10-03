import unittest


# Time: O(n)
# Space: O(1)
def arranging_coins_brute_force(n):
    res, coins = 0, n

    for i in range(1, n + 1):
        if coins < i:
            break
        res += 1
        coins -= i

    return res


def gauss_sum(n):
    return (n / 2) * (n + 1)


# Time: O(logn)
# Space: O(1)
def arranging_coins_gauss(n):
    lo, hi = 1, n

    while lo <= hi:
        mid = (lo + hi) // 2
        required_coins = gauss_sum(mid)

        if required_coins > n:
            hi = mid - 1

        else:
            lo = mid + 1

    return hi


class TestArrangingCoins(unittest.TestCase):
    def test_arranging_coins_brute_force(self):
        self.assertEqual(arranging_coins_brute_force(1), 1)
        self.assertEqual(arranging_coins_brute_force(2), 1)
        self.assertEqual(arranging_coins_brute_force(3), 2)
        self.assertEqual(arranging_coins_brute_force(4), 2)
        self.assertEqual(arranging_coins_brute_force(5), 2)

    def test_arranging_coins_binary_search(self):
        self.assertEqual(arranging_coins_gauss(1), 1)
        self.assertEqual(arranging_coins_gauss(2), 1)
        self.assertEqual(arranging_coins_gauss(3), 2)
        self.assertEqual(arranging_coins_gauss(4), 2)
        self.assertEqual(arranging_coins_gauss(5), 2)


if __name__ == "__main__":
    unittest.main()
