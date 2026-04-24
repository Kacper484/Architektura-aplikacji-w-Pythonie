# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    # TODO: Zwroc instancje Product, np. Product("Laptop", 2999.99, 10)
    return Product("Laptop", 2999.99, 10)
    


# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    # TODO: Uzyj assert product.is_available() == True
    assert product.is_available() == True


def test_total_value(product):
    """Sprawdz wartosc calkowita."""
    # TODO: Uzyj assert product.total_value() == oczekiwana_wartosc
    assert product.total_value() == 29999.9


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    # TODO: Dodaj przypadki testowe jako krotki, np.:
    (5, 15),   # dodanie 5 do poczatkowych 10 = 15
    (0, 10),   # dodanie 0 = bez zmian
    (100, 110),  # dodanie 100
    

])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z roznymi wartosciami."""
    # TODO: Wywolaj product.add_stock(amount) i sprawdz product.quantity
    assert product.add_stock(amount) == expected_quantity


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    """Sprawdz, czy proba usuniecia za duzej ilosci rzuca ValueError."""
    # TODO: Uzyj with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        product.remove_stock(20)


def test_add_stock_negative_raises(product):
    """Sprawdz, czy ujemna wartosc w add_stock rzuca ValueError."""
    # TODO: Uzyj with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        product.add_stock(-5)

# -- testy z zad 1 --


@pytest.mark.parametrize("amount, expected_quantity", [
    # TODO: Dodaj przypadki testowe jako krotki, np.:
    (5, 5),
    (0, 10),
    (10, 0),
])
def test_remove_stock_positive(product, amount, expected_quantity):
    assert product.remove_stock(amount) == expected_quantity


@pytest.fixture
def product2():
    return Product("Telefon", 2999.99, 0)

def test_is_not_available_when_empty(product2):
    assert product2.is_available() == False



# -- Zadanie dodatkowe -- 

@pytest.fixture
def product3():
    return Product("SmartWatch", 200, 10)

@pytest.mark.parametrize("percent, expected_price", [
    (0, 200),
    (50, 100),
    (100, 0), 

])
def test_apply_discount(product3, percent, expected_price):
    product3.apply_discount(percent)
    assert product3.price == expected_price

def test_apply_discount_negative(product3):
    with pytest.raises(ValueError):
        product3.apply_discount(-10)

def test_apply_discount_to_much(product3):
    with pytest.raises(ValueError):
        product3.apply_discount(123)
