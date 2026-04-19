import unittest
import price_calculator as ex5


class TP4PriceCalculatorCases(unittest.TestCase):

    def test_final_price_basic(self):
        # 2 items at $100, 10% discount, 21% tax
        # subtotal=200, after discount=180, after tax=217.8
        self.assertEqual(217.8, ex5.final_price(100, 2, 10, 21))

    def test_final_price_no_discount(self):
        # 1 item at $50, 0% discount, 10% tax
        # subtotal=50, after discount=50, after tax=55.0
        self.assertEqual(55.0, ex5.final_price(50, 1, 0, 10))

    def test_final_price_no_tax(self):
        # 3 items at $30, 20% discount, 0% tax
        # subtotal=90, after discount=72, after tax=72.0
        self.assertEqual(72.0, ex5.final_price(30, 3, 20, 0))

    def test_final_price_rounding(self):
        # 1 item at $33.33, 15% discount, 21% tax
        # subtotal=33.33, after discount=28.3305, after tax=34.279905 → 34.28
        self.assertEqual(34.28, ex5.final_price(33.33, 1, 15, 21))

    def test_best_deal_a_wins(self):
        # A: 1x$100, 50% disc → final with 10% tax = 55.0
        # B: 1x$100, 20% disc → final with 10% tax = 88.0
        self.assertEqual("A", ex5.best_deal(100, 1, 50, 100, 1, 20, 10))

    def test_best_deal_b_wins(self):
        # A: 2x$50, 0% disc → final with 21% tax = 121.0
        # B: 1x$50, 10% disc → final with 21% tax = 54.45
        self.assertEqual("B", ex5.best_deal(50, 2, 0, 50, 1, 10, 21))

    def test_best_deal_equal(self):
        # Same product, same everything → "A"
        self.assertEqual("A", ex5.best_deal(100, 1, 10, 100, 1, 10, 21))


if __name__ == '__main__':
    unittest.main()
