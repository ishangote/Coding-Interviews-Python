import unittest


# Time: O(n)
# Space: O(n)
def reverse_vowels_brute_force(input_string):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    vowels_stack = []
    res = []

    for char in input_string:
        if char in vowels:
            vowels_stack.append(char)

    for char in input_string:
        if char in vowels:
            res.append(vowels_stack.pop())
        else:
            res.append(char)

    return "".join(res)


# Time: O(n)
# Space: O(1)
def reverse_vowels_optimized(input_string):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    input_string = list(input_string)
    lo, hi = 0, len(input_string) - 1

    while lo < hi:
        if input_string[lo] in vowels and input_string[hi] in vowels:
            input_string[lo], input_string[hi] = input_string[hi], input_string[lo]
            lo += 1
            hi -= 1

        if input_string[lo] not in vowels:
            lo += 1

        if input_string[hi] not in vowels:
            hi -= 1

    return "".join(input_string)


class TestReverseVowels(unittest.TestCase):
    def test_reverse_vowels_bf(self):
        self.assertEqual(reverse_vowels_brute_force("IceCreAm"), "AceCreIm")
        self.assertEqual(reverse_vowels_brute_force("leetcode"), "leotcede")

    def test_reverse_vowels_optimized(self):
        self.assertEqual(reverse_vowels_optimized("IceCreAm"), "AceCreIm")
        self.assertEqual(reverse_vowels_optimized("leetcode"), "leotcede")


if __name__ == "__main__":
    unittest.main()
