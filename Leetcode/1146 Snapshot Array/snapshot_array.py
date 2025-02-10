import unittest
from collections import defaultdict
from bisect import bisect_right


class SnapshotArray:
    # Space: O(n + k), where n => length of the array and k => maximum number of unique value snapshots for any index
    def __init__(self, length):
        self.snapshot_array = [[(0, 0)] for itr in range(length)]
        self.snap_id = 0
        pass

    # Time: O(1)
    def set(self, index, value):
        snapshots = self.snapshot_array[index]
        if snapshots and snapshots[-1][0] == self.snap_id:
            snapshots.pop()

        snapshots.append((self.snap_id, value))

    # Time: O(1)
    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def custom_binary_search(self, snapshots, snap_id):
        lo, hi = 0, len(snapshots)

        while lo <= hi:
            mid = (lo + hi) // 2

            if snapshots[mid][0] == snap_id:
                return snapshots[mid][1]

            elif snapshots[mid][0] < snap_id:
                lo = mid + 1

            else:
                hi = mid - 1

        return snapshots[hi][1] if hi >= 0 else 0

    # Time: O(log k), where k => number of unique value snapshots taken for a particular index
    def get(self, index, snap_id):
        snapshots = self.snapshot_array[index]
        return self.custom_binary_search(snapshots, snap_id)


class TestSnapshotArray(unittest.TestCase):
    def test_snapshot_array(self):
        snapshot_array = SnapshotArray(3)
        snapshot_array.set(0, 5)
        snapshot_array.set(0, 8)
        snapshot_array.set(0, 9)
        snapshot_array.set(0, 5)
        self.assertEqual(snapshot_array.snap(), 0)
        snapshot_array.set(0, 6)
        snapshot_array.set(0, 8)
        snapshot_array.set(0, 9)
        self.assertEqual(snapshot_array.snap(), 1)

        self.assertEqual(snapshot_array.get(0, 0), 5)
        self.assertEqual(snapshot_array.get(0, 1), 9)


if __name__ == "__main__":
    unittest.main()
