"""
Questions:
1. Reverse the words not the characters? yes
2. Remove extra whitespaces? No
3. Inplace? Strings are not mutable!!

Examples:

string = 
" hello world!  C++"
          0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.  14.  15.  16.  17.
chars = [' ', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!', ' ', ' ', 'C', '+', '+']

            0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.  14.  15.  16.  17.
reverse = ['+', '+', 'C', ' ', ' ', '!', 'd', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h', ' ']
			                         							        					        s
				                                                                                    e

start_of_word(s) = 0
end_of_word(e) = 3
reverse(0, 2)
s = e

start_of_word(s) = 5
end_of_word(e) = 5
reverse(5, 10)
s = e = 11

start_of_word(s) = 12
end_of_word(e) = 12
reverse(12, 16)
s = e = 17

output = 
"C++  world! hello "

Time: O(n)
Space: O(n)
"""

def reverse(i, j, arr):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def reverse_words(string):
    chars = []
    for ch in string: chars.append(ch)
    reverse(0, len(chars) - 1, chars)
    start_of_word = end_of_word = 0
    
    while start_of_word < len(chars):
        if chars[start_of_word] == ' ':
            start_of_word += 1
            end_of_word = start_of_word
        else:
            while end_of_word < len(chars) and chars[end_of_word] != ' ': end_of_word += 1
            reverse(start_of_word, end_of_word - 1, chars)
            start_of_word = end_of_word
    
    return ''.join(chars)