# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        # TODO: Stworz instancje Product, np. Product("Laptop", 2999.99, 10)
        self.product = Product("Laptop", 2999.99, 10)

    def test_add_stock_positive(self):
        # TODO: Wywolaj add_stock i sprawdz nowa wartosc quantity
        result = self.product.add_stock(5)
        self.assertEqual(result, 15)

    def test_add_stock_negative_raises(self):
        # TODO: Uzyj self.assertRaises(ValueError)
        with self.assertRaises(ValueError):
            self.product.add_stock(-5)

    def test_remove_stock_positive(self):
        # TODO: Wywolaj remove_stock i sprawdz quantity
        result = self.product.remove_stock(3)
        self.assertEqual(result, 7)

    def test_remove_stock_too_much_raises(self):
        # TODO: Uzyj self.assertRaises(ValueError)
        with self.assertRaises(ValueError):
            self.product.remove_stock(20)

    def test_is_available_when_in_stock(self):
        # TODO: Uzyj self.assertTrue
        result = self.product.is_available()
        self.assertTrue(result)

    def test_is_not_available_when_empty(self):
        # TODO: Stworz produkt z quantity=0, uzyj self.assertFalse
        self.p2 = Product("Telefon", 1230.2, 0)
        result = self.p2.is_available()
        self.assertFalse(result)

    def test_total_value(self):
        # TODO: Uzyj self.assertEqual
        result = self.product.total_value()
        self.assertEqual(result, 29999.9)


if __name__ == "__main__":
    unittest.main()
