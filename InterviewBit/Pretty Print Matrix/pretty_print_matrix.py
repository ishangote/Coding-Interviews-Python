# Print concentric rectangular pattern in a 2d matrix. Let us show you some examples to clarify what we mean.
"""
Example 1:
Input: A = 4.
Output:

size = 2 * A - 1

            0 1 2 3 4 5 6

        0   4 4 4 4 4 4 4 
        1   4 3 3 3 3 3 4 
        2   4 3 2 2 2 3 4 
        3   4 3 2 1 2 3 4 
        4   4 3 2 2 2 3 4 
        5   4 3 3 3 3 3 4 
        6   4 4 4 4 4 4 4 

i   j       i   j       i   j       i   j
0   0       1   1(i)    2   2       3   1
0   1       1   2       2   3       
0   2       1   3       24       
0   3       1   4
0   4       1   5 (size - i)
0   5       
0   6   

i -> 0 to size, j -> i to size - i - 1

grid[i][j] = A - i top row
grid[j][i] = A - i left column
grid[size - 1 - i][j] = A - i bottom row
grid[j][size - 1 - i] = A - i right column
"""

def pretty_matrix(num):
    size = 2 * num - 1
    grid = [[False for itr1 in range(size)] for itr2 in range(size)]

    for i in range(size):
        for j in range(i, size - i):
            grid[i][j], grid[j][i], grid[size - 1 - i][j], grid[j][size - 1 - i] = num - i, num - i, num - i, num - i 

    for row in grid:
        print(row)

def main():
    pretty_matrix(3)
    print('\n')

    pretty_matrix(4)
    print('\n')

    pretty_matrix(5)
    print('\n')

    pretty_matrix(6)

if __name__ == '__main__': main()

"""
OUTPUT:
Ishans-MacBook-Pro:Concentric Matrix Print ishangote$ python3 pretty_print_matrix.py 
[3, 3, 3, 3, 3]
[3, 2, 2, 2, 3]
[3, 2, 1, 2, 3]
[3, 2, 2, 2, 3]
[3, 3, 3, 3, 3]


[4, 4, 4, 4, 4, 4, 4]
[4, 3, 3, 3, 3, 3, 4]
[4, 3, 2, 2, 2, 3, 4]
[4, 3, 2, 1, 2, 3, 4]
[4, 3, 2, 2, 2, 3, 4]
[4, 3, 3, 3, 3, 3, 4]
[4, 4, 4, 4, 4, 4, 4]


[5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 5]
[5, 4, 3, 3, 3, 3, 3, 4, 5]
[5, 4, 3, 2, 2, 2, 3, 4, 5]
[5, 4, 3, 2, 1, 2, 3, 4, 5]
[5, 4, 3, 2, 2, 2, 3, 4, 5]
[5, 4, 3, 3, 3, 3, 3, 4, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 5]
[5, 5, 5, 5, 5, 5, 5, 5, 5]


[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6]
[6, 5, 4, 4, 4, 4, 4, 4, 4, 5, 6]
[6, 5, 4, 3, 3, 3, 3, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 2, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 2, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 3, 3, 3, 3, 4, 5, 6]
[6, 5, 4, 4, 4, 4, 4, 4, 4, 5, 6]
[6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
Ishans-MacBook-Pro:Concentric Matrix Print ishangote$ 
"""