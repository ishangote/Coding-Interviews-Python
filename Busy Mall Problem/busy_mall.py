"""
Find the busiest time at the mall given:

        Time        Ppl  Entry/Exit
data = [[1487799425, 14, 1], 
        [1487799425, 4,  0],
        [1487799425, 2,  0],
        [1487800378, 10, 1],
        [1487801478, 18, 0],
        [1487801478, 18, 1],
        [1487901013, 1,  0],
        [1487901211, 7,  1],
        [1487901211, 7,  0] ]

 
 #Eg:

data = [[1487799425, 14, 1], 
        [1487799425, 4,  0],
        [1487799425, 2,  0],
        [1487800378, 10, 1], 
        [1487801478, 18, 0], 
        [1487801478, 18, 1], 
        [1487901013, 1,  0], 
        [1487901211, 7,  1], 
        [1487901211, 7,  0] ] <

max_people_count = 18
max_time_stamp = 1487800378
curr_people_count = 16


"""
import unittest
def busy_mall(data):

        curr_people_count, max_people_count, max_timestamp = 0, 0, 0
        if len(data) == 1: return data[0][0]

        for idx in range(len(data)):
                if data[idx][2] == 0: curr_people_count -= data[idx][1]
                else: curr_people_count += data[idx][1]

                if idx != len(data) - 1 and data[idx + 1][0] != data[idx][0]:
                        if max_people_count < curr_people_count:
                                max_people_count = curr_people_count
                                max_timestamp = data[idx][0]

        return max_timestamp


class TestBusiestMallOutput(unittest.TestCase):
        def test_none_output(self):
                self.assertEqual(busy_mall([]), 0)
        
        def test_one_data_sample(self):
                self.assertEqual(busy_mall([[1487799425, 14, 1]]), 1487799425)

        def test_generic_data(self):
                self.assertEqual(busy_mall([[1487799425, 14, 1], [1487799425, 4,  0], [1487799425, 2,  0], [1487800378, 10, 1], [1487801478, 18, 0], [1487801478, 18, 1], [1487901013, 1,  0], [1487901211, 7,  1], [1487901211, 7,  0]]), 1487800378)


if __name__ == "__main__": unittest.main()