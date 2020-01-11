"""
You are given an array of characters arr that consists of sequences of characters separated by space characters.
Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.
Explain your solution and analyze its time and space complexities.

Example:
input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]

arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
arr[::-1] = ['e', 'c', 'i', 't', 'c', 'a', 'r', 'p', '  ', 's', 'e', 'k', 'a', 'm', '  ', 't', 'c', 'e', 'f', 'r', 'e', 'p']
Reverse each word

"""
#O(n) Space
def sentence_reverse(arr):
    if not arr: return []
    stack, ans = [], []
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == ' ':
            while stack:
                ans.append(stack.pop())
            ans.append(arr[i])
        else:
            stack.append(arr[i])
    
    while stack: ans.append(stack.pop())

    return ans

#O(1) Space
def _sentence_reverse(arr):
    if not arr: return []
    arr = reverse(arr, 0, len(arr) - 1)

    #Find word start index
    start = None
    for i in range(len(arr)):
        if arr[i] == ' ':
            if start != None:
                reverse(arr, start, i - 1)
                start = None

        elif i == len(arr) - 1:
            if start != None:
                reverse(arr, start, i)
        
        else:
            if start == None:
                start = i
    return arr
            
def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

import unittest
class TestSentenceReverse(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(sentence_reverse([' ', ' ']), [' ', ' '])
        self.assertEqual(_sentence_reverse([' ', ' ']), [' ', ' '])
    def test_generic(self):
        self.assertEqual(sentence_reverse(['a', ' ', ' ', 'b']), ['b', ' ', ' ', 'a'])
        self.assertEqual(sentence_reverse(['h', 'e', 'l', 'l', 'o']), ['h', 'e', 'l', 'l', 'o'])
        self.assertEqual(sentence_reverse(["y","o","u"," ","w","i","t","h"," ","b","e"," ","f","o","r","c","e"," ","t","h","e"," ","m","a","y"]), ['m', 'a', 'y', ' ', 't', 'h', 'e', ' ', 'f', 'o', 'r', 'c', 'e', ' ', 'b', 'e', ' ', 'w', 'i', 't', 'h', ' ', 'y', 'o', 'u'])
        self.assertEqual(sentence_reverse(["g","r","e","a","t","e","s","t"," ","n","a","m","e"," ","f","i","r","s","t"," ","e","v","e","r"," ","n","a","m","e"," ","l","a","s","t"]), ["l","a","s","t"," ","n","a","m","e"," ","e","v","e","r"," ","f","i","r","s","t"," ","n","a","m","e"," ","g","r","e","a","t","e","s","t"])

        self.assertEqual(_sentence_reverse(['a', ' ', ' ', 'b']), ['b', ' ', ' ', 'a'])
        self.assertEqual(_sentence_reverse(['h', 'e', 'l', 'l', 'o']), ['h', 'e', 'l', 'l', 'o'])
        self.assertEqual(_sentence_reverse(["y","o","u"," ","w","i","t","h"," ","b","e"," ","f","o","r","c","e"," ","t","h","e"," ","m","a","y"]), ['m', 'a', 'y', ' ', 't', 'h', 'e', ' ', 'f', 'o', 'r', 'c', 'e', ' ', 'b', 'e', ' ', 'w', 'i', 't', 'h', ' ', 'y', 'o', 'u'])
        self.assertEqual(_sentence_reverse(["g","r","e","a","t","e","s","t"," ","n","a","m","e"," ","f","i","r","s","t"," ","e","v","e","r"," ","n","a","m","e"," ","l","a","s","t"]), ["l","a","s","t"," ","n","a","m","e"," ","e","v","e","r"," ","f","i","r","s","t"," ","n","a","m","e"," ","g","r","e","a","t","e","s","t"])
if __name__ == "__main__": unittest.main()