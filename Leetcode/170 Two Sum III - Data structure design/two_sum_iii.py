import unittest


# Space: O(n)
class TwoSum:
    def __init__(self):
        self.nums = {}

    # Time: O(1)
    def add(self, number):
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    # Time: O(n), where n => number of numbers accepted from the stream
    def find(self, target):
        for num in self.nums:
            if target - num in self.nums:
                if target - num == num:
                    if self.nums[target - num] >= 2:
                        return True
                else:
                    return True

        return False


class TestTwoSum(unittest.TestCase):
    def test_two_sum_edge(self):
        two_sum = TwoSum()

        two_sum.add(0)
        self.assertTrue(0 in two_sum.nums)

        self.assertFalse(two_sum.find(0))

    def test_two_sum_1(self):
        two_sum = TwoSum()

        two_sum.add(1)
        self.assertTrue(1 in two_sum.nums)
        two_sum.add(3)
        self.assertTrue(3 in two_sum.nums)
        two_sum.add(5)
        self.assertTrue(5 in two_sum.nums)

        self.assertTrue(two_sum.find(4))
        self.assertFalse(two_sum.find(7))

    def test_two_sum_2(self):
        two_sum = TwoSum()

        two_sum.add(0)
        self.assertTrue(0 in two_sum.nums)
        two_sum.add(-1)
        self.assertTrue(-1 in two_sum.nums)
        two_sum.add(1)
        self.assertTrue(1 in two_sum.nums)

        self.assertTrue(two_sum.find(0))


if __name__ == "__main__":
    unittest.main()
