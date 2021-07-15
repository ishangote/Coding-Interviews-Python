"""
Questions:
1. Case sensetive? Yes

Examples:

str1 = "ZXVVYZW"
str2 = "XKYKZPW" 

longest_subseq
	 ''  Z	X	V	V	Y	Z	W
0 '' '   '  '	'	'	'	'	' 
1 X  '	 '  X   X   X	X	X	X
2 K  '   '  X	X	X	X	X	X
3 Y  '   '	X	X	X	XY	XY	XY
4 K  ' 	 '	X	X	X	XY	XY	XY
5 Z  '	 Z	Z	Z	Z	XY	XYZ	XYZ
6 P  '	 Z	Z	Z	Z	XY	XYZ	XYZ
7 W  '	 Z	Z	Z	Z	XY	XYZ	XYZW

Rule:
if str1[j - 1] == str2[i - 1]: 
    memo[i][j] = memo[i - 1][j - 1] + str1[j - 1]
else:
    memo[i][j] = memo[i - 1][j] if len(memo[i - 1][j]) > len(memo[i][j - 1]) else memo[i][j - 1]

Appending a ch to a string takes O(k) time, k is the len(string)
Why min(n, m) => lcs can be atmost equal to the lenght of the smaller string
Time: O(n * m * min(n, m))
Space: O(n * m * min(n, m))

lengths =
	'' Z X V V Y Z W
0 '' 0 0 0 0 0 0 0 0
1 X  0 0 1 1 1 1 1 1
2 K  0 0 1 1 1 1 1 1
3 Y  0 0 1 1 1 2 2 2
4 K  0 0 1 1 1 2 2 2
5 Z  0 1 1 1 1 2 3 3
6 P  0 1 1 1 1 2 3*3
7 W  0 1 1 1 1 1 1 4*

Build lcs from lengths...
res = ""
if ch1 == ch2:
    res.append(ch1)
    i, j = i-1, j-1
else: 
    i, j = indices of max(lengths[i - 1][j], lengths[i][j - 1])

Time: O(m * n)
Space: O(m * n)
"""
def build_sequence(str1, memo):
    i, j = len(memo) - 1, len(memo[0]) - 1
    res = []
    
    while i != 0 and j != 0:
        if memo[i][j] == memo[i - 1][j]:
            i -= 1
        elif memo[i][j] == memo[i][j - 1]:
            j -= 1
        else:
            res.append(str1[j - 1])
            i -= 1
            j -= 1

    return res[::-1]

def longest_common_subsequence(str1, str2):
    memo = [[0 for j in range(len(str1) + 1)] for i in range(len(str2) + 1)]

    for i in range(1, len(memo)):
        for j in range(1, len(memo[0])):
            if str1[j - 1] == str2[i - 1]:
                memo[i][j] = 1 + memo[i - 1][j - 1]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

    return build_sequence(str1, memo)