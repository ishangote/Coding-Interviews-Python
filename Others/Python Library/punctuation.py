"""
Remove String Punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.)
"""
import string

def remove_string_punctuation(s):
    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
    ans = ""
    for ch in s:
        if ch not in string.punctuation:
            ans += ch
    return ans

import unittest
class TestRemovePunctuation(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(remove_string_punctuation("hello, world"), "hello world")
        self.assertEqual(remove_string_punctuation("hello,  world"), "hello  world")
        self.assertEqual(remove_string_punctuation("hello,world"), "helloworld")

if __name__ == "__main__": unittest.main()