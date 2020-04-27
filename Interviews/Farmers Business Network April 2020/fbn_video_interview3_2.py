"""
Large File:
|--------------------------------------------------------------------|
0                                                                    ∞

Desired Properties:                                                                
No overlaps
Request order maintained                                                       

Ranges:
A. 10k - 20k
B.  1k - 5k
C. 22k - 30k
D. 15k - 25k
E.  2k - 3k
F. 40k - 50k


Overlaps:
 [s, e] 	
   [s1,e1]
[s2,e2]
   []
List:
10-20 -> 1-5 -> 22-30 -> 20-22 -> 40-50   
                                                                                      
func overlap(tup1, tup2) -> return True if overlap

10   99     4    77   45   99    3    44   10  2

			
		10
	 4	    99
		  77
		45

"""