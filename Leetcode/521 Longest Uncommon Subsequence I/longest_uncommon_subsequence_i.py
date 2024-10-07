# Time: O(1)
# Space: O(1)
def longest_uncommon_subsequence(a, b):
    if a == b:
        return -1
    return max(len(a), len(b))
