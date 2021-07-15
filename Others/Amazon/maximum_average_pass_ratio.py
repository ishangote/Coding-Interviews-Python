"""
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.
You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.
The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.
Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. 
The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

Example 2:
Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
 
Constraints:
1 <= classes.length <= 105
classes[i].length == 2
1 <= passi <= totali <= 105
1 <= extraStudents <= 105
"""

"""
Examples:
classes = 
[[1, 2], [3, 5], [2, 2]]
extra = 2

Keep adding 
max_heap = 
[(0.5, 1, 2), (0.6, 3, 5), (1, 2, 2)]
"""
import heapq
def max_avg_pass_ratio(classes, extra_students):
    max_heap = [((x/y), x, y) for [x, y] in classes]
    heapq.heapify(max_heap)
    print(max_heap)

    while extra_students != 0:
        cur_ratio, pass_count, class_count = heapq.heappop(max_heap)
        pass_count += 1
        class_count += 1
        extra_students -= 1
        heapq.heappush(max_heap, ((pass_count / class_count), pass_count, class_count))
        

    print(max_heap)
    
    return sum((x/y) for (_, x, y) in max_heap) / len(classes)

import unittest
class TestMaximumAveragePassRatio(unittest.TestCase):
    def test_generic(self):
        self.assertAlmostEqual(0.78333, max_avg_pass_ratio([[1,2],[3,5],[2,2]], 2))
        self.assertAlmostEqual(0.53485, max_avg_pass_ratio([[2,4],[3,9],[4,5],[2,10]], 4))

if __name__ == "__main__": unittest.main()