"""
You work in a company that prints and publishes books. You are responsible for designing the page numbering mechanism in the printer. You know how many digits a printer can print with the leftover ink. Now you want to write a function to determine what the last page of the book is that you can number given the current page and numberOfDigits left. A page is considered numbered if it has the full number printed on it (e.g. if we are working with page 102 but have ink only for two digits then this page will not be considered numbered).
It's guaranteed that you can number the current page, and that you can't number the last one in the book.

Example
For current = 1 and numberOfDigits = 5, the output should be
pagesNumberingWithInk(current, numberOfDigits) = 5.
The following numbers will be printed: 1, 2, 3, 4, 5.

For current = 21 and numberOfDigits = 5, the output should be
pagesNumberingWithInk(current, numberOfDigits) = 22.
The following numbers will be printed: 21, 22.

For current = 8 and numberOfDigits = 4, the output should be
pagesNumberingWithInk(current, numberOfDigits) = 10.
The following numbers will be printed: 8, 9, 10.
"""

"""
Questions:
1.

Examples:
cur = 
99
digit = 5
ans =
99 100

cur = 1
digits = 5
ans =
1, 2, 3, 4, 5

cur = 21
digits = 5
21, 22

len(21) = 2
cur_digits = 5 - 2 = 3

next_num = 21 + 1 = 22
len(next_num) == 2 <= cur_digits => cur_digits -= 2 = 1

return next num

"""
def pagesNumberingWithInk(current, numberOfDigits):
    cur = str(current)
    while len(cur) <= numberOfDigits:
        numberOfDigits -= len(cur)
        cur = str(int(cur) + 1)
    return int(cur) - 1