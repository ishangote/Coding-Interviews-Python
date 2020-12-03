# Given a string including character: {}[]() return true if it is valid

"""
Valid: {}, (){}, {()}, ...
Invlaid: {, (}, ]()[, ...

# { [ } ]
      ^
hm = {")": "(", "}": "{", "]": "["}
stack = ['{', '[' ]

"""
import unittest
def is_valid_parenthesis(s):
    paren = {')':'(', '}': '{', ']': '['}
    stack = []
    
    for ch in s:
        if ch in paren:
            # Check if stack empty for case input = "}" to avoid list index out of range error
            if not stack or stack[-1] != paren[ch]: return False
            stack.pop()
        else:
            stack.append(ch)
        
    # "return True" not working for edge case input = "{" as stack is not empty after the for loop
    return not stack

if __name__ == "__main__":
    char_set = {'{', '}', '(', ')', '[', ']'}
    s = input("Enter a string with parentheses: ")

    try:
        assert (all(ch in char_set for ch in s))
        print(str(is_valid_parenthesis(s)))
    except:
        print("Invalid input")

    