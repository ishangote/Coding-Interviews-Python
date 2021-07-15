"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
– 1 box of the first type that contains 3 units.
– 2 boxes of the second type that contain 2 units each.
– 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Constraints:
1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106

Hints:
If we have space for at least one box, it’s always optimal to put the box with the most units.
Sort the box types with the number of units per box non-increasingly.
Iterate on the box types and take from each type as many as you can.

=================================================
Approach 1:
Example:
  n, u => n is number of boxes, u is units per box
[[1, 3], [2, 2], [3, 1]]
truckSize = 4

order by units tup[1]
           u  n => ordered by units/box
max_heap [(3, 1), (2, 2), (1, 3)]

capacity = 4
#boxes, #units_per_box = max_heap.pop() {(3, 1)}
ans += min(capacity, #boxes) * #units_per_box (1 * 3) = 3
capacity -= min(capacity, #boxes)


max_heap [(2, 2), (1, 3)]
capacity = 3
#boxes, #units_per_box = max_heap.pop() {(2, 2)}
ans += min(capacity, #boxes) * #units_per_box (2 * 2) = 7
capacity -= min(capacity, #boxes)

max_heap []
capacity = 1
#boxes, #units_per_box = max_heap.pop() {[1, 3]}
ans += min(capacity, #boxes) * #units_per_box (1 * 1) = 8
capacity -= min(capacity, #boxes)       


Time: O(nlogn)
Space: O(n)

=================================================
Approach 2:

Example:
  n, u => n is number of boxes, u is units per box
[[1, 3], [2, 2], [3, 1]]
truckSize = 4

Sort w.r.t #units_per_box
[[1, 3], [2, 2][3, 1]]
                 ^
ans = 8
capacity = 0

Time: O(nlogn)
Space: O(1)
"""

def max_units_on_truck(boxes, capacity):
    boxes.sort(key = lambda x: x[1], reverse = True)

    ans = 0
    for box in boxes:
        if capacity == 0: break
        m = min(box[0], capacity)
        ans += m * box[1]
        capacity -= m
    return ans

import unittest
class TestMaxUnitsOnTruck(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(8, max_units_on_truck([[1, 3], [2, 2], [3, 1]], 4))
        self.assertEqual(91, max_units_on_truck([[5,10],[2,5],[4,7],[3,9]], 10))

if __name__ == "__main__": unittest.main()