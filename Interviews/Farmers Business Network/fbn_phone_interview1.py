"""
FBN Interview

black: 1
white: 0

00001000
00010100
00111110
00000000

11111111
11110111
11111111
11111111

01111111
00010100
00111110
00000000

Constraints:
1. If start point 1: return
"""

def color_image(img, x, y):
    if x >= 0 and x < len(img) and y >= 0 and y < len(img[0]) and img[x][y] == 0: 
        img[x][y] = 0
        color_image(img, x - 1, y)  
        color_image(img, x + 1, y)  
        color_image(img, x, y - 1)  
        color_image(img, x, y + 1)  
        color_image(img, x - 1, y -1) 
        color_image(img, x + 1, y + 1)
    return

def color_image(img, x_start, y_start):
    #Input Validation for x_start, y_start

    stack = [(x_start, y_start)]

    while stack:
        x, y = stack.pop()
        if x >= 0 and x < len(img) and y >= 0 and y < len(img[0]) and img[x][y] == 0:
            img[x][y] = 1

            stack.append((x, y - 1))
            stack.append((x, y + 1))
            stack.append((x - 1, y))
            stack.append((x + 1, y))
            stack.append((x + 1, y + 1))
            stack.append((x - 1, y - 1))
    return