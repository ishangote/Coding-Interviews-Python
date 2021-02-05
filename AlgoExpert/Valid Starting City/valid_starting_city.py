"""
Questions:
1. More than two cities guarnateed? yes
2. Multiple valid starting points? no -> only one starting point will always be valid
3. distances can have -ve or 0? No

Examples:
distances = 
0  1   2   3   4
[5, 25, 15, 10, 15]
^
fuel =
[1, 2, 1, 0, 3]
mpg = 10

5 	   25			     15		10	  15
A	B					C		  D		E ... A
^
*

miles_left = 
1 * 10 = 10
10 - 5 = 5
5 + 2 * 10 = 25
25 - 25 = 0
0 + 1 * 10 = 10
10 < distances[*] (15) -> return False

"""
def valid_starting_city_naive_helper(start_city_idx, distances, fuel, mpg):
    visited_city_count = 0
    miles_left = 0
    cur_city_idx = start_city_idx

    while visited_city_count < len(distances):
        # Visit City
        visited_city_count += 1
        # Fill gas
        miles_left += fuel[cur_city_idx] * mpg
        # Check if we can go to next city
        if miles_left < distances[cur_city_idx]: return False
        # If yes, go to next city 
        miles_left -= distances[cur_city_idx]
        cur_city_idx = (cur_city_idx + 1) % len(distances)

    return True

def valid_starting_city_naive(distances, fuel, mpg):
    #For each city test if it is the correct start
    for city_idx in range(len(distances)):
        if valid_starting_city_naive_helper(city_idx, distances, fuel, mpg): return city_idx

    #If no valid city
    return None

"""
Time: O(n^2), n => number of cities
Space: O(1)
"""