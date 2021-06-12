"""
Questions:
1. input empty? return ""
2. case sensitive? => in = aA => out = 1a1A

Examples:
in = 
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
"A A A A A A A A A A A  A  A  B  B  C  C  C  C  D  D"
 i
                   n

count = 9
 
ans = ""
"""

def run_length_encoding(input_string):
    if not input_string: return ""
    idx = 0
    ans = ""
    while idx < len(input_string):
        next_distinct_idx, count = idx + 1, 1
        while count < 9 and next_distinct_idx < len(input_string) and input_string[idx] == input_string[next_distinct_idx]:
            count += 1
            next_distinct_idx += 1
        
        ans += str(count) + input_string[idx]
        idx = next_distinct_idx

    return ans