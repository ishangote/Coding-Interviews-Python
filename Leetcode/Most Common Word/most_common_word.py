# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
# Words in the list of banned words are given in lowercase, and free of punctuation.  
# Words in the paragraph are not case sensitive.  The answer is in lowercase.
"""
Example:
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
"""
from collections import Counter
import string
def most_common_word(paragraph, banned):
    banned = set(banned)

    for ch in paragraph:
        if ch in string.punctuation:
            paragraph = paragraph.replace(ch, " ")
    
    paragraph = [word for word in paragraph.lower().split() if word not in banned]

    count = Counter(paragraph)

    return count.most_common(1)[0][0]
        
import unittest
class TestMostCommonWord(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]), "ball")
        self.assertEqual(most_common_word("a, a, a, a, b,b,b,c, c", ["a"]), "b")

if __name__ == "__main__": unittest.main()