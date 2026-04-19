import unittest
import number_to_month as ex2


class TP5NumberToMonthCases(unittest.TestCase):
    def test_number_to_month(self):

        result0 = ex2.number_to_month(0)
        result1 = ex2.number_to_month(1)
        result2 = ex2.number_to_month(2)
        result3 = ex2.number_to_month(3)
        result4 = ex2.number_to_month(4)
        result5 = ex2.number_to_month(5)
        result6 = ex2.number_to_month(6)
        result7 = ex2.number_to_month(7)
        result8 = ex2.number_to_month(8)
        result9 = ex2.number_to_month(9)
        result10 = ex2.number_to_month(10)
        result11 = ex2.number_to_month(11)
        result12 = ex2.number_to_month(12)
        result13 = ex2.number_to_month(13)
        self.assertEqual("error", result0)
        self.assertEqual("enero", result1)
        self.assertEqual("febrero", result2)
        self.assertEqual("marzo", result3)
        self.assertEqual("abril", result4)
        self.assertEqual("mayo", result5)
        self.assertEqual("junio", result6)
        self.assertEqual("julio", result7)
        self.assertEqual("agosto", result8)
        self.assertEqual("septiembre", result9)
        self.assertEqual("octubre", result10)
        self.assertEqual("noviembre", result11)
        self.assertEqual("diciembre", result12)
        self.assertEqual("error", result13)


if __name__ == '__main__':
    unittest.main()
