"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:
A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
"""
"""
Questions:
1. path a string? -> yes
2. path contains only chars U, D -> yes

Examples:

01234567
UDDDUDUU
        ^
altitude = 0
count = 1

if altitude becomes zero after coming from down then weh ahve completed a valley

Time: O(n)
Space: O(1)

"""
def counting_valleys(steps, path):
    altitude = 0
    count = 0

    for stp in path:
        if stp == 'U':
            altitude += 1
            if altitude == 0: count += 1
        else:
            altitude -= 1
        
    return count