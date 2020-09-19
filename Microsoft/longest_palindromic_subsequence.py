"""
SUBSEQUENCE: NOT CONTIGUOUS

Given a string s, find the longest palindromic subsequence's length in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
 

Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

            bbbab
                    ""
                b
            bb    bb
        bbb            
    bbba

What is the longest palindroming subsequence between row and col:

0 1 2 3 4 5
a g b d b a

l = 1 => row = col => 1

l = 2

   0 1 2 3 4 5        
0  1 1 
1    1 1 
2      1 1
3        1 1
4          1 1
5            1

l = 3

2 2 4
b d b

2 + 1 = 3

   0 1 2 3 4 5        
0  1 1 1 
1    1 1 1
2      1 1 3 
3        1 1 1
4          1 1
5            1


l = 4

   0 1 2 3 4 5        
0  1 1 1 1 
1    1 1 1 3
2      1 1 3 3
3        1 1 1
4          1 1
5            1


l = 5

   0 1 2 3 4 5        
0  1 1 1 1 3
1    1 1 1 3 3
2      1 1 3 3
3        1 1 1
4          1 1
5            1


l = 6

   0 1 2 3 4 5        
0  1 1 1 1 3 5
1    1 1 1 3 3
2      1 1 3 3
3        1 1 1
4          1 1
5            1

if s[i] == s[j]:
    memo[i][j] = memo[i + 1][j - 1] + 2
else:
    memo[i][j] = max(memo[i + 1][j - 1], memo[i][j - 1])


4648658D3D8C

"""