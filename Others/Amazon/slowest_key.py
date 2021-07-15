"""
Examples:
              0123
keyPressed = "cbcd"
                0   1   2   3
releaseTimes = [9, 29, 49, 50]
                           i

durations = {
    c: 20,
    b: 20
    d: 1
}

Time: O(n)
Space: O(n)
"""
from collections import defaultdict
import sys
def slowest_key(keys_pressed, release_times):
    if len(keys_pressed) != len(release_times): return None
    durations = defaultdict(lambda: 0)
    durations[keys_pressed[0]] = release_times[0]

    for i in range(1, len(release_times)):
        durations[keys_pressed[i]] = max(durations[keys_pressed[i]], release_times[i] - release_times[i - 1])

    max_time = -sys.maxsize
    max_key = ""
    for k in durations:
        if durations[k] > max_time: 
            max_time = durations[k]
            max_key = k
    
    for k in durations:
        if durations[k] == max_time and ord(k) - ord('a') > ord(max_key) - ord('a'): 
            max_key = k
    
    return max_key

import unittest
class TestSlowestKeys(unittest.TestCase):
    def test_generic(self):
        self.assertEqual("c", slowest_key("cbcd", [9, 29, 49, 50]))
        self.assertEqual("a", slowest_key("spuda", [12, 23, 36, 46, 62]))

if __name__ == "__main__": unittest.main()