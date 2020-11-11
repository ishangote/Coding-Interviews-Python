from house_robber_ii import house_robber_ii_naive
import unittest

"""
[200,3,140,20,10]
340
"""

class TestHouseRobberII(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(house_robber_ii_naive([2, 3, 2]), 3)
        