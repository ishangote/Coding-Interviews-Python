# Given a string, find the length of the longest substring without repeating characters.
# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
valid => no chars repating

0 1 2 3 4 5 6 7
a b c a b c b b

a
abc
abca
abcab

b
bc
bca
bcab
...
Brute Force: O(n^3)
valid_substr(curr) -> return True if valid else False

chars_set = {a, b, c}
max_length = 
0 1 2 3 4 5 6 7
a b a c b c b b
      i 
          j 
"""

def longest_substr(input_str):
    #Input Validations
    chars_set = set()
    i, j = 0, 0 
    max_len = 0

    while j < len(input_str) and i < len(input_str):
        while input_str[j] in chars_set:
            chars_set.remove(input_str[i])
            i += 1

        else:
            chars_set.add(input_str[j])
            max_len = max(max_len, j - i + 1)
            j += 1

    return max_len

"""
Feedback:
Communication
[11:09] what is a continuous substring
[11:09] return 0 when input is empty
[11:10] rephrase the problem 
[11:11] can single char be a valid substring
[11:16] visual illustration
[11:19] need to have a better time awareness
[11:23] spend too long going over the example

Problem Solving
[11:11] find all substrings and check each substring => O(n^3)
[11:14] sliding window approach because there are overlap values
[11:16] set is a good ds here -> Why?

Coding
[11:24] start coding
[11:28] finish coding


Verification
"""