from collections import Counter

# Time: O(n + m), n => length of ransom_note and m => length of magazine
# Space: O(m)
def ransom_note(ransom_note, magazine):
    magazine_char_count = Counter(magazine)

    for char in ransom_note:
        if char not in magazine_char_count or magazine_char_count[char] <= 0: return False
        magazine_char_count[char] -= 1

    return True

# ------------------------------------------------------------ #

import unittest
class TestRansomNote(unittest.TestCase):
    def test_ransom_note(self):
        self.assertEqual(ransom_note("a", "b"), False)
        self.assertEqual(ransom_note("aa", "ab"), False)
        self.assertEqual(ransom_note("aa", "aab"), True)
        
if __name__ == "__main__": unittest.main()