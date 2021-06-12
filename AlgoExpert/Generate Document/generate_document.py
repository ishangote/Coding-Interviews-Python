"""
Questions:
1. white spaces in characters counted? yes
2. can characters be counted multiple times? no
3. case sensetive chars? yes

Examples:
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
ans = True

-----------------------

characters = "helloworldO "
document = "hello wOrld"
ans = True

characters = "helloworldO "
document = "hello wOrld"
ans = True

char_counts = {
	h: 1
	e: 1
	l: 3
	o: 2
	w: 1
	r: 1
	d: 1
	O: 1
	' ': 1
}

Time: O(n + m), n => number of chars in document
Space: O(m), m => number of chars in characters
"""

def generate_document(characters, document):
    char_counts = {}
    for ch in characters:
        if ch in char_counts: char_counts[ch] += 1
        else: char_counts[ch] = 1

    for ch in document:
        if ch not in char_counts or char_counts[ch] == 0: return False
    
    return True