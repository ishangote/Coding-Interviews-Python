# Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, 
# sorted by the number of occurrences in a descending order. 
# If two or more words have the same count, they should be sorted according to their order in the original sentence. 
# Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word. 
# The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words. Analyze the time and space complexities of your solution. 
# Try to optimize for time while keeping a polynomial space complexity.
"""
Example:

"Practice makes perfect. you'll only get Perfect by practice. just practice!"

[["practice", "3"], ["perfect", "2"], ["makes", "1"], ["youll", "1"], ["only", "1"], ["get", "1"], ["by", "1"], ["just", "1"]]
"""

import string
def pre_process(input_string):
    tr = str.maketrans("", "", string.punctuation)      #Removes Punctuations
    input_string = input_string.translate(tr).lower()   # All lower case
    
    # Or ...
    # punctuation = ",.:;?!'"
    # words = [w.strip(punctuation).lower() for w in words]

    return ' '.join(input_string.split())               # Removes only tabs and new_lines. Keeps spaces

from collections import Counter
def word_count_engine_using_library(input_string):
    if not input_string: return None
    input_string = pre_process(input_string)
    return Counter(input_string.split()).most_common()

def word_count_engine_using_hm(input_string):
    if not input_string: return None
    hm = {}
    input_string = pre_process(input_string)

    for word in input_string.split():
        if word in hm: hm[word] += 1
        else: hm[word] = 1

    # To sort in reverse -> 
    return sorted(hm.items(), key = lambda x: x[1], reverse = True)

    # Or ...
    # word_freq = []
    # for key, value in hm.items():
    #     word_freq.append((value, key))

    # word_freq.sort(reverse = True)
    # return word_freq

import unittest
class TestWordCountEngine(unittest.TestCase):
    text = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
    result = [("practice", 3), ("perfect", 2), ("makes", 1), ("youll", 1), ("only", 1), ("get", 1), ("by", 1), ("just", 1)]

    def test_invaid_input(self):
        self.assertEqual(word_count_engine_using_library(""), None)
        self.assertEqual(word_count_engine_using_hm(""), None)

    def test_generic_word_count_input(self):
        self.assertEqual(word_count_engine_using_library(self.text), self.result)
        self.assertEqual(word_count_engine_using_hm(self.text), self.result)

if __name__ == "__main__": unittest.main()