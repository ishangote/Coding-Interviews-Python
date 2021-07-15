"""
'G': go straight 1 unit
'L': turn 90 degrees to left
'R': turn 90 degrees to right

Examples:
instructions = "GGLLGG"
output = true
(0, 0) -> (0, 1) -> (0, 2) -> (turns 90 degrees left) -> (turns 90 degrees left) -> (0, 1) -> (0, 0)


instructions = "GG"
output = false
(0, 0) -> (0, 1) -> (0, 2) -> ....

instructions = "GL"
output = true
(0, 0) -> (0, 1) -> (turns 90 degrees left) -> (-1, 1) -> (turns 90 degrees left) -> (-1, 0) -> (turns 90 degrees left) -> (0, 0)
       G          L                         G           L                         G          L                           G

if robot returns to same position then in circle? yes
limit cycle trajectory math => 
after max 4 cycles the robot must return to its original location OR
at end of cycle 1 the direction of robot must not be equal to initial direction
"""

def robot_limit_cycle(instructions):
    (x, y) = (0, 0)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #^up, down, right, left
    #^x,y  x,y  x, -y, -x, y
    #[0]   [1]   [2]    [3]
    d = 0

    for i in instructions:
        if i == "G":
            x += directions [d%4][0]
            y += directions [d%4][1]
        #^move through the directions bound within of 4 places in the plane
        elif i == "R":
            d += 1 #increment the direction by one place
        elif i == "L":
            d -= 1 #decrease by one place
            
    return (x, y) == (0, 0) or d%4 != 0 