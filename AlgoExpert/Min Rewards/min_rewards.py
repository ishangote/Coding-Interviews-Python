"""
Questions:
1. Are duplicates in scores? No
2. Are scores sorted? No
3. Are scores positive? Yes

Examples:
scores = 
[8, 4, 2, 1, 3, 6, 7, 9, 5]
    	                 i
	   				  j
awards = 
[1]
[2, 1]
[3, 2, 1]
[4, 3, 2, 1]
[4, 3, 2, 1, 2]
[4, 3, 2, 1, 2, 3]
[4, 3, 2, 1, 2, 3, 4]
[4, 3, 2, 1, 2, 3, 4, 5]
[4, 3, 2, 1, 2, 3, 4, 5, 1]

res = sum(awards) = 25

while iterating backwards(j):
awards[j] = max(awards[j], awards[j + 1] + 1)

Time: O(n^2), n => len(scores)
Space: O(n)

------------------------------------------------------

Optimization: Peaks/Valleys Technique
scores = 
[8, 4, 2, 1, 3, 6, 7, 9, 5]
      <-  V ->			 V
[4	3  2  1  2  3  4  5   ]


[8, 4, 2, 1, 3, 6, 7, 9, 5]
      	   V 	 	   <-V->
[4  3  2  1  2  3  4  5  1]
	  
Get all valley points and iterate to left and right of each valley by incrementing the awards

Time: O(n)
Space: O(n)
------------------------------------------------------

Cleanest Optimization:

scores = 
[8, 4, 2, 1, 3, 6, 7, 9, 5]
awards = 
[1, 1, 1, 1, 1, 1, 1, 1, 1]

forward pass => 
scores = 
[8, 4, 2, 1, 3, 6, 7, 9, 5]
                      i
awards = 
[1, 1, 1, 1, 2, 3, 4, 5, 1]

backward pass => 
scores = 
[8, 4, 2, 1, 3, 6, 7, 9, 5]
 i
awards = 
[4, 3, 2, 1, 2, 3, 4, 5, 1]

Time: O(n)
Space: O(n)
"""
def minRewards(scores):
    awards = [1] * len(scores)
    #Forward Pass
    for i in range(1, len(scores)):
        if scores[i - 1] < scores[i]: awards[i] = max(awards[i], 1 + awards[i - 1])

    # Backward Pass
    for j in range(len(scores) - 2, -1, -1):
        if scores[j] > scores[j + 1]: awards[j] = max(awards[j], 1 + awards[j + 1])

    return sum(awards)