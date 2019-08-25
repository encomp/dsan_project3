import unittest

from problem1.SquareRoot import sqrt


class SquareRootTest(unittest.TestCase):

    def test_sqrt_of_negative_number(self):
        self.assertIsNone(sqrt(-188))

    def test_sqrt_of_0(self):
        self.assertEqual(0, sqrt(0))

    def test_sqrt_of_9(self):
        self.assertEqual(3, sqrt(9))

    def test_sqrt_of_16(self):
        self.assertEqual(4, sqrt(16))

    def test_sqrt_of_1(self):
        self.assertEqual(1, sqrt(1))

    def test_sqrt_of_27(self):
        self.assertEqual(5, sqrt(27))

    def test_sqrt_of_40(self):
        self.assertEqual(6, sqrt(40))

    def test_sqrt_of_70(self):
        self.assertEqual(8, sqrt(70))

    def test_sqrt_of_81(self):
        self.assertEqual(9, sqrt(81))


if __name__ == '__main__':
    unittest.main()
