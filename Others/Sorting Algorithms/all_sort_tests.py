import unittest
from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from selection_sort import selectionSort
import random

class TestAllSorts(unittest.TestCase):
    def test_empty_input(self):
        print("Testing edge cases...")
        self.assertEqual(bubbleSort([]), [])
        self.assertEqual(insertionSort([]), [])
        self.assertEqual(selectionSort([]), [])

    def test_large_inputs(self):
        print("Testing large inputs...")
        random_list = random.sample(range(-800000, 800000), 10000)
        sorted_random_list = sorted(random_list)
        self.assertEqual(bubbleSort(random_list), sorted_random_list)
        self.assertEqual(insertionSort(random_list), sorted_random_list)
        self.assertEqual(selectionSort(random_list), sorted_random_list)

if __name__ == "__main__": unittest.main()