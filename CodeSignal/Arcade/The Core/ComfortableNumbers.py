"""
Let's say that number a feels comfortable with number b if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.
How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [l, r], and each number feels comfortable with the other (so a feels comfortable with b and b feels comfortable with a)?

Example
For l = 10 and r = 12, the output should be
comfortableNumbers(l, r) = 2.

Here are all values of s(x) to consider:
s(10) = 1, so 10 is comfortable with 9 and 11;
s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.
Thus, there are 2 pairs of numbers comfortable with each other within the segment [10; 12]: (10, 11) and (11, 12).
"""
def dig_sum(x):
    digs = list(str(x))
    return sum(int(dig) for dig in digs)
    
def is_comfortable(x, y):
    if x == y: return False
    dig_sum_x = dig_sum(x)
    return x - dig_sum_x <= y <= x + dig_sum_x

def comfortableNumbers(l, r):
    ans = 0
    for a in range(l, r):
        for b in range(a + 1, r + 1):
            if is_comfortable(a, b) and is_comfortable(b, a): 
                ans += 1
    return ans