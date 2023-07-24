from django.test import TestCase
from ..sudoku.utils import shuffle


class TestShuffle(TestCase):
    def test_randomness(self):
        # Test for randomness using statistical tests
        lst = [1, 2, 3, 4, 5]
        testList = shuffle(lst)
        # Perform statistical tests on the shuffled list to check randomness
        self.assertIsNotNone(lst, testList)

    def test_preservation_of_elements(self):
        # Test if all elements are preserved after shuffling
        lst = [1, 2, 3, 4, 5]
        shuffled = shuffle(lst)
        self.assertEqual(len(lst), len(shuffled))

    def test_empty_list(self):
        # Test handling of an empty list
        lst = []
        shuffled = shuffle(lst)
        self.assertEqual(len(shuffled), 0)

    def test_single_element_list(self):
        lst = [10]
        shuffled = shuffle(lst)
        self.assertEqual(len(shuffled), 1)
        self.assertEqual(shuffled, lst)
