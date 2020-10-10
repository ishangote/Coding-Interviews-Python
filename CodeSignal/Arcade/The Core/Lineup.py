"""
To prepare his students for an upcoming game, the sports coach decides to try some new training drills. To begin with, he lines them up and starts with the following warm-up exercise: when the coach says 'L', he instructs the students to turn to the left. Alternatively, when he says 'R', they should turn to the right. Finally, when the coach says 'A', the students should turn around.
Unfortunately some students (not all of them, but at least one) can't tell left from right, meaning they always turn right when they hear 'L' and left when they hear 'R'. The coach wants to know how many times the students end up facing the same direction.
Given the list of commands the coach has given, count the number of such commands after which the students will be facing the same direction.

Example
For commands = "LLARL", the output should be
lineUp(commands) = 3.
"""
"""
Questions:
1. Input has a string "LRA"? -> yes
2. Lowercase uppercase? -> always uppercase
3. How many students are defaulters? -> Atleast 1
4. Do they all stand facing the same direction initially? -> Yes

Examples:

Simulate for two guys a, b, b is idiot

0: facing front
1: facing left
2: facing back
3: facing right

"""
def lineUp(commands):
    a, b = 0, 0
    ans = 0
    for cmd in commands:
        if cmd == 'A':
            a += 2
            b += 2
        
        elif cmd == 'L':
            a += 1
            b -= 1
            #Normalizing to keep b in range(3)
            b += 4
        
        else:
            a -= 1
            b += 1
            a += 4
        
        #More normalizing
        a %= 4
        b %= 4
        if a == b: ans += 1
    
    return ans

"""
Time: O(n)
Space: O(1)
"""