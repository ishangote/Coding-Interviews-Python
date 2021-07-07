"""
Questions:
1. "", "a" palindrome? yes
2. Substrings are contiguous? yes

Examples:
Naive Solution: Check for all substrings, if palindrome?
Time: O(n^3)
Space: O(1)

string = 
0 1 2 3 4 5 6 7 8 9
a b a x y z z y x f
      i			
	  			j

max_len = 6
max_palin = "xyzzyx"

---------------------------------

string = 
0 1 2 3 4 5 6 7 8 9
a b a x y z z y x f
      i 
                j

max_len = 6
max_palin = "xyzzyx"

Time: O(n^2)
Space: O(n)
"""
def get_palindrome_at_index(i, j, input_string):
    cur_palindrome = ""
    while 0 <= i < len(input_string) and 0 <= j < len(input_string) and input_string[i] == input_string[j]:
        cur_palindrome = input_string[i: j + 1]
        i -= 1
        j += 1
    return cur_palindrome

def longest_plaindrome(string):
    if not string: return ""
    max_len_palin = ""
    for i in range(len(string)):
        odd_palin = get_palindrome_at_index(i, i, string)
        if len(odd_palin) > len(max_len_palin):
            max_len_palin = odd_palin

        even_palin = get_palindrome_at_index(i, i + 1, string)
        if len(even_palin) > len(max_len_palin):
            max_len_palin = even_palin

    return max_len_palin