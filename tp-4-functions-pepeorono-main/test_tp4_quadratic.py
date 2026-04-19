import unittest
import quadratic as ex3


class TP5QuadraticCases(unittest.TestCase):
    def test_roots(self):
        result1 = ex3.roots(1, -3, 2)  # Retorna: "(2.0, 1.0)"
        result2 = ex3.roots(1, -2, 1)  # Retorna: "(1.0)"
        result3 = ex3.roots(1, 2, 3)  # Retorna: "( )"
        self.assertEqual("(2.0, 1.0)", result1)
        self.assertEqual("(1.0)", result2)
        self.assertEqual("( )", result3)

    def test_value_y(self):
        result1 = ex3.value_y(1, -3, 2, 0)  # Retorna: 2
        result2 = ex3.value_y(1, -3, 2, 1)  # Retorna: 0
        result3 = ex3.value_y(1, -3, 2, -1)  # Retorna: 6
        self.assertEqual(2, result1)
        self.assertEqual(0, result2)
        self.assertEqual(6, result3)

    def test_to_string(self):
        result1 = ex3.to_string(2, -3, 1)  # Retorna: "f(x) = 2 * X^2 + -3 * X + 1"
        result2 = ex3.to_string(0, 4, -1)  # Retorna: "f(x) = 4 * X + -1"
        result3 = ex3.to_string(0, 0, 5)  # Retorna: "f(x) = 5"
        result4 = ex3.to_string(2, 0, 5)  # Retorna: "f(x) = 2 * X^2  + 5"
        self.assertEqual("f(x) = 2 * X^2 + -3 * X + 1", result1)
        self.assertEqual("f(x) = 4 * X + -1", result2)
        self.assertEqual("f(x) = 5", result3)
        self.assertEqual("f(x) = 2 * X^2 + 5", result4)

    def test_derivation(self):
        result1= ex3.derivation(2, -3, 1)  # Retorna: "f'(x) = 4 * X + -3"
        result2= ex3.derivation(0, 4, -1)  # Retorna: "f'(x) = 4"
        result3= ex3.derivation(0, 0, 5)  # Retorna: "f'(x) = 0"
        result4= ex3.derivation(2, 0, 5)  # Retorna: "f'(x) = 4 * X"
        self.assertEqual("f'(x) = 4 * X + -3", result1)
        self.assertEqual("f'(x) = 4", result2)
        self.assertEqual("f'(x) = 0", result3)
        self.assertEqual("f'(x) = 4 * X", result4)


if __name__ == '__main__':
    unittest.main()
