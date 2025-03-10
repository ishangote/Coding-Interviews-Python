import unittest


# Time: O(n), where n => length of array
# Space: O(1)
def monotonic_array_single_pass(arr):
    if len(arr) < 2:
        return True

    direction = None

    for idx in range(1, len(arr)):
        if arr[idx - 1] > arr[idx]:
            if not direction:
                direction = "DECREASING"
            elif direction == "INCREASING":
                return False

        elif arr[idx - 1] < arr[idx]:
            if not direction:
                direction = "INCREASING"
            elif direction == "DECREASING":
                return False

    return True


class TestMonotonicArray(unittest.TestCase):
    def test_monotonic_array(self):
        self.assertTrue(monotonic_array_single_pass([1, 2, 2, 3]))
        self.assertTrue(monotonic_array_single_pass([6, 5, 4, 4]))
        self.assertTrue(monotonic_array_single_pass([1, 1, 1]))
        self.assertFalse(monotonic_array_single_pass([1, 3, 2]))


if __name__ == "__main__":
    unittest.main()
