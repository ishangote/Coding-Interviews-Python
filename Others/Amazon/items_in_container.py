"""
Given a string s consisting of items as "*" and closed compartments as an open and close "|", an array of starting indices startIndices, and an array of ending indices endIndices, 
determine the number of items in closed compartments within the substring between the two indices, inclusive.
An item is represented as an asterisk *
A compartment is represented as a pair of pipes | that may or may not have items between them.

Example:
s = '|**|*|*'
startIndices = [1,1]
endIndices = [5,6]

s = 
0   1   2   3   4   5   6
|   *   *   |   *   |   * 


range (0, 5) => 
s[0:6] = "|**|*|"
          i
             j
            items = 2
"""
def number_of_items(s):
    pass

def items_in_containers(s, start_idx, end_idx):
    res = []
    for (i, j) in zip(start_idx, end_idx):
        res.append(number_of_items(s[i: j + 1]))
    return res