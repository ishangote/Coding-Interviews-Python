import unittest
import heapq


# Time: O(m + n), where m => number of rows, n => number of cols
# Space: O(1)
def count_of_elements_lte(mid, matrix):
    row, col = len(matrix) - 1, 0
    count = 0

    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] <= mid:
            count += row + 1
            col += 1
        else:
            row -= 1

    return count


# Time: O((m + n) * log(max_num - min_num)), where m = number of rows, n => number of cols,
#   max_num => matrix[-1][-1],
#   min_num => matrix[0][0]
# Space: O(1)
def kth_smallest_element_in_sorted_matrix_binary_search(matrix, k):
    lo, hi = matrix[0][0], matrix[-1][-1]

    while lo < hi:
        mid = (lo + hi) // 2

        if count_of_elements_lte(mid, matrix) >= k:
            hi = mid
        else:
            lo = mid + 1

    return lo


# ------------------------------------------------------------------------ #


# Time: O(m*n*log(m)), where m => number of rows, n => number of cols
# Space: O(m)
def kth_smallest_element_in_sorted_matrix_min_heap(matrix, k):
    min_heap = [(matrix[row][0], row, 0) for row in range(len(matrix))]
    heapq.heapify(min_heap)  # O(n)

    for _ in range(k - 1):
        (_, row, col) = heapq.heappop(min_heap)

        if col == len(matrix[0]) - 1:
            continue

        heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

    return min_heap[0][0]


# ------------------------------------------------------------------------ #


# Time: O(n*mlog(k)), where n => number of rows, m => number of cols
# Space: O(k)
def kth_smallest_element_in_sorted_matrix_max_heap(matrix, k):
    max_heap = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            heapq.heappush(max_heap, -1 * matrix[row][col])

            if len(max_heap) > k:
                heapq.heappop(max_heap)

    return -1 * heapq.heappop(max_heap)


class TestKthSmallestElementInSortedMatrix(unittest.TestCase):
    def test_kth_smallest_element_in_sorted_matrix_binary_search(self):
        self.assertEqual(
            kth_smallest_element_in_sorted_matrix_binary_search(
                [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8
            ),
            13,
        )

    def test_kth_smallest_element_in_sorted_matrix_min_heap(self):
        self.assertEqual(
            kth_smallest_element_in_sorted_matrix_min_heap(
                [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8
            ),
            13,
        )

    def test_kth_smallest_element_in_sorted_matrix_max_heap(self):
        self.assertEqual(
            kth_smallest_element_in_sorted_matrix_max_heap(
                [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8
            ),
            13,
        )


if __name__ == "__main__":
    unittest.main()
