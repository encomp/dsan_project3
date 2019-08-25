import unittest

from problem2.RotatedSorted import rotated_array_search


class RotatedSortedTest(unittest.TestCase):

    @staticmethod
    def linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1

    def setUp(self) -> None:
        self.rarray_1 = [6, 7, 8, 9, 10, 1, 2, 3, 4]
        self.rarray_2 = [6, 7, 8, 1, 2, 3, 4]

    def test_search_in_rotated_array_one_number_6(self):
        self.assertEqual(self.linear_search(self.rarray_1, 6), rotated_array_search(self.rarray_1, 6))

    def test_search_in_rotated_array_one_number_9(self):
        self.assertEqual(self.linear_search(self.rarray_1, 9), rotated_array_search(self.rarray_1, 9))

    def test_search_in_rotated_array_one_number_7(self):
        self.assertEqual(self.linear_search(self.rarray_1, 7), rotated_array_search(self.rarray_1, 7))

    def test_search_in_rotated_array_one_number_8(self):
        self.assertEqual(self.linear_search(self.rarray_1, 8), rotated_array_search(self.rarray_1, 8))

    def test_search_in_rotated_array_one_number_1(self):
        self.assertEqual(self.linear_search(self.rarray_1, 1), rotated_array_search(self.rarray_1, 1))

    def test_search_in_rotated_array_one_number_4(self):
        self.assertEqual(self.linear_search(self.rarray_1, 4), rotated_array_search(self.rarray_1, 4))

    def test_search_in_rotated_array_one_number_3(self):
        self.assertEqual(self.linear_search(self.rarray_1, 3), rotated_array_search(self.rarray_1, 3))

    def test_search_in_rotated_array_one_number_2(self):
        self.assertEqual(self.linear_search(self.rarray_1, 2), rotated_array_search(self.rarray_1, 2))

    def test_search_in_rotated_array_one_number_200(self):
        self.assertEqual(-1, rotated_array_search(self.rarray_1, 200))

    def test_search_in_rotated_array_two_number_8(self):
        self.assertEqual(self.linear_search(self.rarray_2, 8), rotated_array_search(self.rarray_2, 8))

    def test_search_in_rotated_array_two_number_1(self):
        self.assertEqual(self.linear_search(self.rarray_2, 1), rotated_array_search(self.rarray_2, 1))

    def test_search_in_rotated_array_two_number_10(self):
        self.assertEqual(self.linear_search(self.rarray_2, 10), rotated_array_search(self.rarray_2, 10))

    def test_search_in_rotated_array_two_number_12(self):
        self.assertEqual(-1, rotated_array_search(self.rarray_2, 12))


if __name__ == '__main__':
    unittest.main()
