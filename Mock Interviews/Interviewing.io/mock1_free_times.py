# Given a list of people's busy times, find the FREE times that are common across everyone's schedules.

# My code during interview:
"""
def free_times(timestamps):
    tmp = []
    for t in timestamps:
        tmp.extend(t)
        
    tmp.sort(key = lambda x: x[0])
    
    ans = set()
    for i in range(len(tmp) - 1):
        if tmp[i][1] < tmp[i + 1][0]: 
            ans.add((tmp[i][1], tmp[i + 1][0]))
    
    return list(ans)

test1 = [[(1,2)], [(5, 6)]]
# Expected = [(2, 5)]
test2 = [[(2, 3), (6, 7)], [(0, 4), (5, 6)], [(1, 2), (6, 7), (8, 9)]]
# Expected = [(4, 5), (7, 8)]
test3 = [[(1,2), (5, 6)]]
test4 = [[(2, 3)], [(3, 6)]]
print(free_times(test2))
"""

# Solving the problem later...
"""
maximum of latest end time so far must be tracked!

timestamps 
[(0, 4), (1, 2), (2, 3), (5, 6), (6, 7), (6, 7), (8, 9)]
     ^
"""
# Corrections to code:
def get_timeline(timestamps):
  tmp = []
  for t in timestamps:
    tmp.extend(t)

  tmp.sort(key = lambda x: x[0])
  return tmp

def free_times(timestamps):
  ans = set()
  timestamps = get_timeline(timestamps)
  latest_end_time = 0

  for i in range(len(timestamps) - 1):
    latest_end_time = max(latest_end_time, timestamps[i][1])
    if timestamps[i + 1][0] > latest_end_time:
      ans.add((latest_end_time, timestamps[i + 1][0]))

  return list(ans)
    
import unittest
class TestFreeTimes(unittest.TestCase):
  def test_generic(self):
    self.assertEqual(free_times([[(2, 3), (6, 7)], [(0, 4), (5, 6)], [(1, 2), (6, 7), (8, 9)]]), [(4, 5), (7, 8)])

if __name__ == "__main__": unittest.main()

"""
Feedback:
Would you advance this person to the next round (e.g. onsite)? *
No
How were their technical skills? 
Solid
How was their problem solving ability? 
Solid
What about their communication ability? 
Amazing!
Help your interviewee get better! 
Because interviewing.io requires us to grade candidates on a strict rubric, 
I would not advance this candidate because he wasn't able to complete the problem in time, but he did a good job overall. 
If this interview was part of a panel of interviews, I would've been supportive of advancing the candidate 
if his performance was good in the other ones, because I received good signals on most of the attributes.

Good job doing the following things (keep doing these!):
- You walked through your approach visually by writing out examples, which made your explanations easy to follow.
- Great instinct to process the input in a way that would be easier to wade through, i.e. combining the intervals into one flat list and sorting them. 
This is a common approach to simplifying problems with nested input that makes it easier for you to find a solution.
- Sharing your thoughts while you coded - You did a good job keeping me in the loop while you wrote your solution by 
explaining why you were implementing things a certain way, which allowed me to see your decision-making process as you figured out how to code your approach. 
Sharing your thoughts also allows the interviewer to jump in and help you out if you had gone off-track or gotten stuck.

Practice the following things to improve your interviewing skills:
- Scrap your approach if it starts getting complicated. - You came up with a straightforward solution with an O(nlogn) runtime, 
but when you double-checked to see if you could improve the runtime, you fixated on an approach to iterate through the elements with a set, 
which got overcomplicated when you tried to figure out how to properly determine overlaps. Once you realized that it would be 
difficult to efficiently find overlaps, you should have just moved forward with your O(nlogn) solution, instead of spending time trying to make it work. 
If it's hard to explain, then it'll be hard to code, so it's most likely not the best approach. 
You only have limited time in an interview, so use your time wisely and move on! 
If you're not sure if your solution is the best one, but it's very easy to explain and isn't very inefficient (O(nlogn) isn't a terrible runtime), 
then move forward with it for now, and you can note optimizations in the end if you have time.

- Break down the solution into multiple helper methods when there are distinct operations happening, i.e. combining the intervals into a sorted list can be a separate helper method. 
This makes the code even cleaner to read, makes it easier to debug, and shows that you care about code quality. Don't overstress it 
during the interview though if you haven't confirmed if you have a working solution yet, but it's good to call it out during an interview so the interviewer can see that you're mindful of this.
"""