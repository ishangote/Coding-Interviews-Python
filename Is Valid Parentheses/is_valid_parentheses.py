# Given a string including character: {}[]() return true if it is valid

"""
Valid: {}, (){}, {()}, ...
Invlaid: {, (}, ]()[, ...

# { [ } ]
      ^
hm = {")": "(", "}": "{", "]": "["}
stack = ['{', '[' ]

"""