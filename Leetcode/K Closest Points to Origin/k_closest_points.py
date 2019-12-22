# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

"""
[[3,3],[5,-1],[-2,4]] k = 2

Approach 1:
sort points according to dist and return first k points

Approach 2:
min heap ->
            (-26, [5, -1]) <- pop

            (-20, [-2, 4])
            (-9, [3, 3])
            
"""

def k_closest_points(points, k):
    points.sort(key = lambda p:p[0]**2 + p[1]**2)
    return points[:k]

#---------------------------------------------

import heapq
def k_closest_points_heap(points, k):
    heap = []
    for point in points:
        dist = - (point[0]**2 + point[1]**2)
        heapq.heappush(heap, [dist, point])
        if len(heap) > k: heapq.heappop(heap)

    return [point for [dist, point] in heap]

#---------------------------------------------

import unittest
class TestKClosestPointsToOrigin(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(k_closest_points([], 2), [])
        self.assertEqual(k_closest_points_heap([], 2), [])

        self.assertEqual(k_closest_points([[-2, 3]], 2), [[-2, 3]])
        self.assertEqual(k_closest_points_heap([[-2, 3]], 2), [[-2, 3]])
    
    def test_equal_dist_points(self):
        self.assertEqual(k_closest_points([[-2, 4], [2, -4], [-9, 3]], 2), [[-2, 4], [2, -4]])
        self.assertEqual(k_closest_points_heap([[-2, 4], [2, -4], [-9, 3]], 2), [[-2, 4], [2, -4]])

    def test_k_closest_points_generic(self):
        self.assertEqual(k_closest_points([[1,3],[-2,2]], 1), [[-2,2]])
        self.assertEqual(k_closest_points([[3,3],[5,-1],[-2,4]], 2), [[3,3],[-2,4]])

if __name__ == "__main__": unittest.main()