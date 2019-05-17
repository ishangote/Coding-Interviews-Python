"""


        0  1  2  3
    0   Q
    1         Q
>   2                *backtrack
    3

postitions = [[0,0], [1, 2], ]



        0  1  2  3
    0   Q
    1            Q
    2      Q
>   3               *backtrack



postitions = [[0,0], [1, 3]]

        0  1  2  3
    0   Q
    1            Q
    2      Q
>   3               *backtrack



postitions = [[0,0], [1, 3], [2, 1]]

        0  1  2  3
>   0      Q
    1               *backtrack
    2               *backtrack
    3               *backtrack

postitions = [[0, 1], ]



        0  1  2  3
    0      Q
    1            Q   
    2   Q            
>   3         Q            

postitions = [[0, 1], [1, 3], [2, 0], [3, 2]]
return

"""

positions = []
def is_safe(i, j):
    
def n_queens_util(n, row, posititons):

    