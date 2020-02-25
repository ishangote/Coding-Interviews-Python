"""
          1
    2              3
  4   5       6       7
8  9   10       11  12  13
                          14
                            15

1, 3, 2, 4, 5, 6, 7, 13, 12, 11, 10, 9, 8, 14, 15



s_even [7, 6, 5, 4]
s_odd  [ ]


			a						a c b d e f
        b		c 
      d  e     f g

s1 = []
s2 = []
"""

class BinaryTreeNode:
    def __init__(self, val):
  	    self.val = val
        self.left = None
        self.right = None

def spiral_binary_tree(root):
    if not root: return []
    stack1, stack2 = [root], []
    ans = []
    while stack1 or stack2:
        while stack1:
            node = stack1.pop()
            ans.append(node.val)

            if node.left: stack2.append(node.left)
            if node.right: stack2.append(node.right)

        while stack2:
            node = stack2.pop()
            ans.append(node.val)

            if node.right: stack1.append(node.right)
            if node.left: stack1.append(node.left)
      
    return ans
"""
TESTING:
root = None -> []

ans = [a, c, b, e, f]

root = a
      b	c
     e 	 f
s1 = []
s2 = []

"""
"""
Feedback:
Intro was still not sleek, mentioned "want to deploy software"

Hinting at trying to use DFS instead of saying "modification of BFS"

Kept insisting on using stack instead of saying why we are trying to use stack

Kept saying "I" instead of "we"

Would be good to mention direction of python stack

Instead of starting with 1 stack, ideal flow of logical thinking would have been starting with 1 queue (BFS) and then intead use 2 stacks after identifying the problem of maintaining level info. From this interviewer can easily make out you knew the solution (minor point, does not matter if the interviewer thinks so in many cases, shows preparation)

It would have been clearer if you had labeled levels as 0, 1, 2, etc and called the two stacks as stack_even, stack_odd etc.

"So what I do is" <-- stop saying I so much


python library dequeu

kept insisting on using deque, instead of taking the interviewers hint of not using deque

Don't ask for whether to write the tree class, shows lazyness (it's a small class, not like a large algo)
It helps understand the structure better

In between you say  "Then I will check"


Stumbled saying unit tests. Still need practice to be sleek.

"I enter our program" Why I???

Cough, say excuse me.

Based on testing it seems like the code works --> incorrect statment. Say so the code seems to be working for this test example

Also when you take test example, write the test example and expected answer before diving into the code to compute actual value

Test1. 
Input:
Expected Output:

Work out:
Actual Output:
Why do you want to join this company?
Not sleek answer

Good answer for disagreement:
"His"  ---> RED FLAG, always say "his or her"

Used the word "Deploy" too much
git is a bit noob question 

CI (Continuous Integeration)
CD (Continuous Deployment)

After joining, typically, how long does it take for new hires to start contributing to production code? are there any trainings?
 

Feedback:
Behavioral:
	1. Typically for a new hire, how long does it take a new hire to ramp up on training?
	2. Disgreement red flag: His or her -> NEVER only HIS!
    3. CI(Continuous integration), CD(Continuous deployment)

"""