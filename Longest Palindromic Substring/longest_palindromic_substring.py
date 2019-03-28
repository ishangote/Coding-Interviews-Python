# Given a string return the length of the longest palindromic SUBSTRING (Continuous)
# On^2

"""
Expand around each character(odd) and each two characters(even)
0  1  2  3  4  5
i 
j
a  b  a  a  b  c
               ^
               ^
1  3  4  1  1  1

"""
import unittest
def longest_palindromic_substring(input_string):
    max_length = 0
    longest_palin = ''
    for idx in range(len(input_string)):
        #Odd expansion
        odd_palin, max_odd_len = get_max_palin_substr(input_string, idx, idx)
        #Even expansion
        even_palin, max_even_len = get_max_palin_substr(input_string, idx, idx + 1)

        # Return the string =>
        if len(longest_palin) < len(odd_palin): longest_palin = odd_palin
        elif len(longest_palin) < len(even_palin): longest_palin = even_palin

        # Return the max length =>    
        # max_length = max(max_length, max_even_len, max_odd_len)
    
    # return max_length
    return longest_palin

def get_max_palin_substr(input_string, left_idx, right_idx):

    while left_idx >= 0 and right_idx < len(input_string) and input_string[left_idx] == input_string[right_idx]:
        left_idx -= 1
        right_idx += 1
    
    # Return palin, length
    return input_string[left_idx + 1 : right_idx], right_idx - left_idx - 1


class TestLongestPalindromicSubString(unittest.TestCase):
    def test_empty_string(self):
        # self.assertEqual(longest_palindromic_substring(""), 0)
        self.assertEqual(longest_palindromic_substring(""), '')
    
    def test_one_char_string(self):
        # self.assertEqual(longest_palindromic_substring("a"), 1)
        self.assertEqual(longest_palindromic_substring("a"), 'a')

    def test_long_string(self):
        # self.assertEqual(longest_palindromic_substring("banana"), 5)
        self.assertEqual(longest_palindromic_substring("banana"), "anana")

if __name__ == "__main__":unittest.main()