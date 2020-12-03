# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

"""
Questions:
1. Is empty string valid? len(input) >= 1
2. Does input have any other char? No 

Examples:

Input:
"("
Output:
False

Input:
")"
Output:
False

Input:
"(}"
Output:
False

Input:
")("
Output:
False

Input:
")("
Output:
False

Input:
"({[]})"
Output:
True


Input:
"()[{}]"
Output:
True

Input:
"()[{}]"
      ^
stack = None => True

Input:
"[}{]"
  ^
stack =
[

Pseudo:
isValid(str:input) -> True/False
    stack = []
    for each char in input:
        if char in ")}]":
            if stack top not corresponding open bracket: return False
            else pop stack
        else:
            stack push char

Time: O(n)
Space: O(n)

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