# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""

# ========================================
# from annotationlib import get_annotate_from_class_namespace
# Szkielet pliku: product.py
# Uzupelnij implementacje!
# ========================================

from selectors import SelectSelector
from unittest.mock import AsyncMockMixin
class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # TODO: Zapisz atrybuty name, price, quantity
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        self.name = name
        if price >= 0:
            self.price = price
        
        if quantity >= 0:
            self.quantity = quantity
        

    def add_stock(self, amount: int):
        # TODO: Dodaj ilosc do magazynu. Rzuc ValueError jesli amount < 0
        if amount >= 0:
            self.quantity += amount
            return self.quantity
        else:
            raise ValueError

        

    def remove_stock(self, amount: int):
        # TODO: Usun ilosc z magazynu.
        # Rzuc ValueError jesli amount < 0 lub amount > quantity
        if amount >= 0 and amount <= self.quantity:
            self.quantity -= amount
            return self.quantity
        else:
           raise ValueError

    def is_available(self) -> bool:
        # TODO: Zwroc True jesli quantity > 0
        if self.quantity > 0:
            return True
        else:
            return False


    def total_value(self) -> float:
        # TODO: Zwroc price * quantity
        return round(self.price * self.quantity, 2)


# -- Zadanie dodatkowe -- 

    def apply_discount(self, percent: float) -> float:
        if percent == 0 :
            return round(self.price, 1)
            
        if 0 <= percent <= 100:
            discount = self.price * (percent/100)
            self.price -= discount
            return round(self.price, 1)
        else:
            raise ValueError
