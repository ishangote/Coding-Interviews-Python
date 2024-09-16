# Time: O(n), n => length of s & t
# Space: O(n)
def isomorphic_strings(s, t):
    if len(s) != len(t): return False

    st_char_map, ts_char_map = {}, {}

    for idx in range(len(s)):
        s_char, t_char = s[idx], t[idx]
        if (s_char in st_char_map and st_char_map[s_char] != t_char) or (t_char in ts_char_map and ts_char_map[t_char] != s_char):
            return False

        st_char_map[s_char] = t_char
        ts_char_map[t_char] = s_char

    return True

import unittest
class TestIsomorphicStrings(unittest.TestCase):
    def test_isomorphic_strings(self):
        self.assertEqual(isomorphic_strings("", ""), True)
        self.assertEqual(isomorphic_strings("paper", "title"), True)
        
        self.assertEqual(isomorphic_strings("pappr", "title"), False)
        self.assertEqual(isomorphic_strings("badc", "baba"), False)

if __name__ == "__main__": unittest.main()
