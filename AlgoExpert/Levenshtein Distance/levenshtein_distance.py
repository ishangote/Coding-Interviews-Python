"""
Questions:
1. both strings empty: return 0

Examples:
operations = 
	0  1 2 3 4
	'' y a b d 
0 ''0  1 2 3 4
1 a 1  1 1 2 3
2 b 2  2 2 1 2
3 c 3  3 3 2 2

if s1[i - 1] != s2[j - 1]:
	ops[i][j] = 1 + min(ops[i - 1][j], ops[i][j - 1], ops[i - 1][j - 1])
else:
	ops[i][j] = ops[i - 1][j - 1]

ans = ops[-1][-1]
"""

def levenshtein_distance(str1, str2):
    operations = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(len(operations)):
        operations[i][0] = i
    
    for j in range(len(operations[0])):
        operations[0][j] = j
    
    for i in range(1, len(operations)):
        for j in range(1, len(operations[0])):
            if str1[i - 1] == str2[j - 1]: operations[i][j] = operations[i - 1][j - 1]
            else:
                operations[i][j] = 1 + min(operations[i - 1][j], operations[i - 1][j - 1], operations[i][j -1])
    
    return operations[-1][-1]