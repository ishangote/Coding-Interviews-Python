# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
"""
Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.


["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]

{
    the:4
    day:1
    is:3
    sunny:2
}

max_heap = [(-4, 'the'), (-3, 'is'), (-2, 'sunny'), (-1, 'day')]

"""
import heapq
def top_k_frequent_words(words, k):
    count_map = {}
    max_heap = []
    #O(n)
    for w in words:
        if w not in count_map:
            count_map[w] = 1
        else:
            count_map[w] += 1

    #O(n)
    # heapq.heapify(x) Transform list x into a heap, in-place, in linear time.
    max_heap = [(-freq, word) for (word, freq) in count_map.items()]
    heapq.heapify(max_heap)
    

    ans = []
    #O(nlogk)
    for i in range(k):
        ans.append(heapq.heappop(max_heap)[1])

    return ans
    
import unittest
class TestTopKFrequentWords(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(top_k_frequent_words(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4), ["the","is","sunny","day"])
        self.assertEqual(top_k_frequent_words(["i", "love", "leetcode", "i", "love", "coding"], 2), ["i", "love"])

if __name__ == "__main__": unittest.main()