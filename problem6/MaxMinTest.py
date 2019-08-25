import random
import unittest

from problem6.MaxMin import get_min_max


class MaxMinTest(unittest.TestCase):

    def new_random_array(self, start, end):
        l = [i for i in range(start, end)]
        random.shuffle(l)
        return l

    def test_case_one(self):
        array = self.new_random_array(0, 10)
        self.assertEqual((0, 9), get_min_max(array))

    def test_case_two(self):
        array = self.new_random_array(5, 100)
        self.assertEqual((5, 99), get_min_max(array))

    def test_case_three(self):
        array = self.new_random_array(1, 1000)
        self.assertEqual((1, 999), get_min_max(array))

    def test_case_four(self):
        array = [4, 6, 2, 5, 9, 8]
        self.assertEqual((2, 9), get_min_max(array))

    def test_case_five(self):
        array = [0, 4, 6, 2, 5, 9, 88]
        self.assertEqual((0, 88), get_min_max(array))

    def test_array_is_none(self):
        self.assertIsNone(get_min_max(None))

    def test_array_is_empty(self):
        self.assertIsNone(get_min_max([]))

    def test_array_is_too_small(self):
        self.assertIsNone(get_min_max([1]))

    def test_array_with_two_elements(self):
        self.assertEqual((0, 9), get_min_max([0, 9]))

    def test_array_with_same_min_and_max(self):
        self.assertIsNone(get_min_max([9, 9, 9, 9]))


if __name__ == '__main__':
    unittest.main()
