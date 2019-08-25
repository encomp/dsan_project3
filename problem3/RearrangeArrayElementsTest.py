import unittest

from problem3.RearrangeArrayElements import rearrange_digits


class RearrangeArrayElementsTest(unittest.TestCase):

    def test_first_array(self):
        result = rearrange_digits([4, 6, 2, 5, 9, 8])
        self.assertEqual([964, 852], result)

    def test_first_array_sorted(self):
        result = rearrange_digits([2, 4, 5, 6, 8, 9])
        self.assertEqual([964, 852], result)

    def test_second_array_sorted(self):
        result = rearrange_digits([1, 2, 3, 4, 5])
        self.assertEqual([531, 42], result)

    def test_second_array(self):
        result = rearrange_digits([5, 4, 3, 2, 1])
        self.assertEqual([531, 42], result)

    def test_none_array(self):
        self.assertIsNone(rearrange_digits(None))

    def test_array_with_one_element(self):
        self.assertIsNone(rearrange_digits([1]))

    def test_array_with_two_elements(self):
        self.assertEqual([2, 1], rearrange_digits([1, 2]))

    def test_array_with_three_elements(self):
        self.assertEqual([31, 2], rearrange_digits([3, 1, 2]))


if __name__ == '__main__':
    unittest.main()
