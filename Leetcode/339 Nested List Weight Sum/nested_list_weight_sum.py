import unittest


def recursive_helper(nested_list, depth):
    res = 0

    for ele in nested_list:
        res += ele * depth if isinstance(ele, int) else recursive_helper(ele, depth + 1)

    return res


# Time: O(n), where n => number of integers in the structure
# Space: O(d), where d => maximum depth of the nested list structure
def nested_list_weight_sum(nested_list):
    return recursive_helper(nested_list, 1)


class TestNestedListWeightSum(unittest.TestCase):
    def test_nested_list_weight_sum(self):
        self.assertEqual(nested_list_weight_sum([1, 2, 3, 4]), 10)
        self.assertEqual(nested_list_weight_sum([1, [4, [6]]]), 27)
        self.assertEqual(nested_list_weight_sum([[1, 1], 2, [1, 1]]), 10)
        self.assertEqual(nested_list_weight_sum([1, [4, [6, 1, [5, 1]]]]), 54)


if __name__ == "__main__":
    unittest.main()
