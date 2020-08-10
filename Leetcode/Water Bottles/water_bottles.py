# Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Return the maximum number of water bottles you can drink.
"""
Example 1:
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Example 2:
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.

Example 3:
Input: numBottles = 5, numExchange = 5
Output: 6

Example 4:
Input: numBottles = 2, numExchange = 3
Output: 2


numBottles = 9, numExchange = 3


exchange(empty_bottles): return[full_bottles, remaining_empty_bottles] else return False

"""
def exchange(empty_bottles, exchange_rate):
    if exchange_rate > empty_bottles: return False
    full_bottles = empty_bottles // exchange_rate
    empty_bottles = empty_bottles % exchange_rate
    return [full_bottles, empty_bottles]


def num_water_bottles(initial_full_bottles, exchange_rate):
    ans = initial_full_bottles
    empty_bottles = initial_full_bottles

    while True:
        excg = exchange(empty_bottles, exchange_rate)
        if not excg: return ans
        full_bottles, empty_bottles = excg[0], excg[1]
        ans += full_bottles
        empty_bottles += full_bottles

import unittest
class TestWaterBottles(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(num_water_bottles(9, 3), 13)
        self.assertEqual(num_water_bottles(13, 3), 19)

if __name__ == "__main__": unittest.main()