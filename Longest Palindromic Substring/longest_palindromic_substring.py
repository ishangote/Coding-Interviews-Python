# Given a string return the length of the longest palindromic SUBSTRING (Continuous)

"""
0  1  2  3  4  5
i 
j
a  b  a  a  b  c
^


"""

def longest_palindromic_substring(input_string):

    for idx in range(len(input_string)):
        #Odd expansion
        max_odd_len = get_max_palin_substr(input_string, idx, idx)
        #Even expansion
        max_even_len = get_max_palin_substr(input_string, idx, idx + 1)

        max_length = max(max_even_len, max_odd_len)

    return max_length

def get_max_palin_substr(input_string, left_idx, right_idx):

    while left_idx >= 0 and right_idx < len(input_string) and input_string[left_idx] == input_string[right_idx]:
        left_idx -= 1
        right_idx += 1

    return right_idx - left_idx - 1


def main():
    print(longest_palindromic_substring("abaabc"))

if __name__ == "__main__":main()
