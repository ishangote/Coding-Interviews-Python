import unittest


# Time: O(26 * n), where n => length of s2
# Space: O(26) ~ O(1)
def permutation_in_string(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_count, s2_count = [0] * 26, [0] * 26
    lo = 0

    # Initialize both frequency arrays for the first len(s1) characters
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord("a")] += 1
        s2_count[ord(s2[i]) - ord("a")] += 1

    if s1_count == s2_count:
        return True

    # Start sliding the window
    for hi in range(len(s1), len(s2)):
        s2_count[ord(s2[hi]) - ord("a")] += 1  # Expand window
        s2_count[ord(s2[lo]) - ord("a")] -= 1  # Shrink window
        lo += 1  # Move the left pointer

        if s1_count == s2_count:
            return True

    return False


class TestPermutationInString(unittest.TestCase):
    def test_permutation_in_string(self):
        self.assertTrue(permutation_in_string("ab", "eidbaooo"))
        self.assertFalse(permutation_in_string("ab", "eidboaoo"))
        self.assertTrue(permutation_in_string("abc", "xyadcbamn"))


if __name__ == "__main__":
    unittest.main()
