'''
You are given a list of projects and a list of dependencies (which is a list of pairs of projects, 
where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. 
Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
Input:

  	projects: [a,b,c,d,e,f]
    dependencies: [(a,d), (f,b), (b,d), (f,a), (d,c)]
    							
Output: f,e,a,b,d,c

{
a:d
f:b, a
b:d
d:c
}

{
a:f
b:f
c:d
d:b
e:None
f:None
}
    
a,b,c,d,e,f
  ^
  
a -> b
	<-
          
			f b a e c d

      f -> a ->e
      |		 |   |
      *    *   *
      b	-> d <-c
            
s = [a, b]

[f, b, d, a, e]

(a,d)	=> a -> d

(f,b) => f -> b

Could not solve further...
'''

# For solution refer to Course Schedule II in Leetcode