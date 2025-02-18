import unittest
import heapq


# Time: O(nlogk), where n => number of points
# Space: O(k)
def k_closest_points_to_origin(points, k):
    max_heap = []

    for point in points:
        distance = point[0] * point[0] + point[1] * point[1]

        heapq.heappush(max_heap, (-1 * distance, point))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [point for _, point in max_heap]


class TestKClosestPointsToOrigin(unittest.TestCase):
    def test_k_closest_points_to_origin(self):
        self.assertEqual(k_closest_points_to_origin([], 2), [])
        self.assertEqual(k_closest_points_to_origin([[-2, 3]], 2), [[-2, 3]])

        self.assertEqual(
            sorted(k_closest_points_to_origin([[-2, 4], [2, -4], [-9, 3]], 2)),
            sorted([[-2, 4], [2, -4]]),
        )

        self.assertEqual(
            sorted(k_closest_points_to_origin([[3, 3], [5, -1], [-2, 4]], 2)),
            sorted([[3, 3], [-2, 4]]),
        )


if __name__ == "__main__":
    unittest.main()
