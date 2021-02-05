"""
Questions:
1. Powerset -> Set of all subsets -> does order matter? No
2. is Emptyy set a subset? Yes

Examples:
nums = 
[1]
powerset = [[], [1]]

nums = [1, 2]
powerset = [[], [1], [2], [1, 2]]


nums = 
[1, 2, 3]
 ^
powerset = 
[[]]
[[], [1]]
[[], [1], [2], [1, 2]]
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


Init powerset = [[]]
generate cur_subset by appending cur number to all existing subsets in powerset
"""
def powerset_iterative(nums):
    powerset = [[]]

    for num in nums:    
        subsets_containing_num = []
        for subset in powerset:
            subsets_containing_num.append(subset + [num])

        powerset.extend(subsets_containing_num)

    return powerset



"""
Time: O(2^n * n)
Space: O(2^n * n)

How? -> 
[[]]                                                            1
[[], [1]]                                                       2
[[], [1], [2], [1, 2]]                                          4
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]          8
                                                                16
                                                                ...
                                                                2^n

Each subset has on average n/2 numbers => O(2^n * n/2) ~ O(2^n * n)

"""