"""
Questions:
1. Atleast 2 students? yes
2. Input mutable? yes
3. strictly taller => if heights are equal return false

Examples:
red = 
[5, 8, 1, 3, 4]
blue = 
[6, 9, 2, 4, 5]

Sort both =>
[1, 3, 4, 5, 8]
[2, 4, 5, 6, 9]

--------------------------
red = 
[2, 7, 8]
blue = 
[1, 7, 6]

Sort both =>
[2, 7, 8]
[1, 6, 7]

return False -> Not correct

Sort Reverse =>
[8, 7, 2]
[7, 6, 1]

return True
"""

def validate(arr1, arr2):
    for (n1, n2) in zip(arr1, arr2):
        if n1 <= n2: return False
    return True

def class_photos(red, blue):
    # Input validations
    red.sort(reverse = True)
    blue.sort(reverse = True)
    return validate(red, blue) or validate(blue, red)