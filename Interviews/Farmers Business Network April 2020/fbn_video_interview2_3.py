"""
Palindrome:

bob
A man, a plan, a canal... Panama!
1331

browser plugin  -->  stream  -->  palincheck
simple text palindromes (characters, numbers)

Deployment: very small docker, 128 MB RAM  $ <-- pal_check runs here

bool pal_check(in: InStream):

inStream.get()  -> char, EOF, raise StopIteration, etc.

Input:
in.get() -> A
in.get() -> 
in.get() -> m
A man, a plan, a canal... Panama!

tmp = [a, m, a, n, a, p,...]

[b, a, a, a, a, b]			

return tmp == tmp[::-1]

alphanumeric -> Valid
else
"""

def be_check(in):
	tmp = []
	while ch := in.get():
		if ch.isalnum(): tmp.append(ch.lower())
	
	return tmp == tmp[::-1]

"""
Palincoin --> stream --> palincheck ~1 GB

superxlarge, 16 GB RAM  $$$   <-- be_check runs here

bool pal_check(inStream in, outStream out):

outStream.put(char) --> cloud storage  $0

bool dispatch(outStream)  $$$$ --> invokes the BE node, converts outStream to inStream
	bool be_check(inStream in)

bool pal_check(inStream in, outStream out):

A man, a plan, a canal... Panama!
abba
abab
^
"""

def pal_check(in, out):
    count = 0
	tmp = []
	while ch := in.get() and count < 10000:
		if ch.isalnum():
            tmp.append(ch.lower())
            count += 1
        out.put(ch)

    if count < 10000: return tmp == tmp[::-1]

	while ch := in.get():
		if ch.isalnum():
		out.put(ch)
	
	return dispatch(out)