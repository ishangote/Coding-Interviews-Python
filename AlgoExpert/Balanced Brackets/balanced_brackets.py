"""
Questions:
1. if string == ""? return true

Examples:
Balanced => [], ([]), {()[]}
Unbalanced => [}, )(, [(])

eg. 1
([])
  ^
stack = ['(', '[']

([])
    ^
stack = [] => return True

-------------------------

eg. 2
[(])
  ^
stack = ['[', '('] => return False

-------------------------

eg. 3
([]{})
  ^
stack = ["(", "["]

([]{})
    ^
stack = ["(", "{"]

([]{})
     ^
stack = ["("]

([]{})
     ^
stack = [] => return True

-------------------------
eg. 4
([{
  ^
stack = ["(", "[", "{"]
"""

def balanced_brackets(string):
    bracks = ["[", "]", "(", ")", "{", "}"]
    matching_bracks = {"}": "{", ")": "(", "]": "["}
    stack = []

    for i in range(len(string)):
        if string[i] not in bracks: continue
        if string[i] in matching_bracks:
            if not stack or stack[-1] != matching_bracks[string[i]]: return False
            stack.pop()
        else: stack.append(string[i])
    
    return not stack