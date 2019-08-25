import copy
import unittest

from problem4.DutchNationalFlag import sort_012


class DutchNationalFlagTest(unittest.TestCase):

    def assertSorted(self, array):
        new_copy = copy.deepcopy(array)
        sort_012(new_copy)
        self.assertEqual(sorted(array), new_copy)

    def test_sort_case_one(self):
        array = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
        self.assertSorted(array)

    def test_sort_case_two(self):
        array = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
        self.assertSorted(array)

    def test_sort_case_three(self):
        array = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        self.assertSorted(array)

    def test_sort_case_four(self):
        array = [2, 2, 2, 1, 1, 1, 0, 0, 0]
        self.assertSorted(array)

    def test_sort_case_five(self):
        array = [2, 1, 0, 2, 1, 0, 2, 1, 0]
        self.assertSorted(array)

    def test_small_array(self):
        array = [2, 1, 0]
        self.assertSorted(array)

    def test_none_array(self):
        self.assertIsNone(sort_012(None))

    def test_array_of_one_element(self):
        self.assertIsNone(sort_012([0]))

    def test_array_of_two_elements(self):
        self.assertIsNone(sort_012([0, 1]))


if __name__ == '__main__':
    unittest.main()
