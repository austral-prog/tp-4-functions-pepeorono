import unittest.mock
import maximums as ex1


class TP5MaximumsCases(unittest.TestCase):

    def test_maximums(self):
        result1 = ex1.max_of_two(5, 4)
        self.assertEqual(5, result1)

        result2 = ex1.max_of_two(-2, -3)
        self.assertEqual(-2, result2)

        result3 = ex1.max_of_two(0, 0)
        self.assertEqual(0, result3)

        result4 = ex1.max_of_three(5, 4, 7)
        self.assertEqual(7, result4)

        result5 = ex1.max_of_three(-2, -3, -1)
        self.assertEqual(-1, result5)

        result6 = ex1.max_of_three(0, 0, 0)
        self.assertEqual(0, result6)


if __name__ == '__main__':
    unittest.main()
