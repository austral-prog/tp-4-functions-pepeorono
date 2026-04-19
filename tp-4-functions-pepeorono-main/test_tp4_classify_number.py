import unittest
import classify_number as ex4


class TP4ClassifyNumberCases(unittest.TestCase):

    def test_positive_even(self):
        self.assertEqual("positive even", ex4.classify_number(4))
        self.assertEqual("positive even", ex4.classify_number(100))

    def test_positive_odd(self):
        self.assertEqual("positive odd", ex4.classify_number(3))
        self.assertEqual("positive odd", ex4.classify_number(99))

    def test_negative_even(self):
        self.assertEqual("negative even", ex4.classify_number(-2))
        self.assertEqual("negative even", ex4.classify_number(-50))

    def test_negative_odd(self):
        self.assertEqual("negative odd", ex4.classify_number(-1))
        self.assertEqual("negative odd", ex4.classify_number(-77))

    def test_zero(self):
        self.assertEqual("zero", ex4.classify_number(0))


if __name__ == '__main__':
    unittest.main()
