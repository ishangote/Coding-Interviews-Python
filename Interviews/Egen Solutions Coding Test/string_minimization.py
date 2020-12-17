"""
Questions:
1. len(input) == 0/1?  no (2 <= len <= 10^5)
2. case sensitive? all lowercase letters

Examples:
input = 
abbz
output = 
4

------------

input = 
abba

l    h
a   bba => 
bb

l h
b b =>

""
output = 
0

------------

input = 
0 1 2 3 4 5 6 7 8 9
a a b c c c a b b a =>
    l
                h

bcccabb =>
0 1 2 3 4 5 6 7 8 9
a a b c c c a b b a =>
      l
            h

ccca (Can not reduce further)

output =
4

------------

input = 
0 1 2 3
a b b a
  r
    h

output = 
0
"""
import string
def string_minimization(input_string):
    assert 2 <= len(input_string) <= 10 ** 5
    assert all(ch in string.ascii_lowercase for ch in input_string)
    
    lo, hi = 0, len(input_string) - 1

    while lo < hi and input_string[lo] == input_string[hi]:
        ch = input_string[lo]
        while lo < hi and input_string[lo] == ch:
            lo += 1
        #Test input == abba -> need to run hi pointer 1 pos before lo
        while lo <= hi and input_string[hi] == ch:
            hi -= 1

    return hi - lo + 1

if __name__ == "__main__":
    myString = input("Enter a string in lowercase chars: ")
    print("After string minimization...")
    print(string_minimization(myString))

"""
Time: O(n), n = length of input string
Space: O(1)
"""