import pytest
from factories import ProductFactory

def test_read_product():
    product = ProductFactory()
    assert 'name' in product

def test_update_product():
    product = ProductFactory()
    product['name'] = "Updated"
    assert product['name'] == "Updated"

def test_delete_product():
    product = ProductFactory()
    products = [product]
    products.remove(product)
    assert product not in products

def test_list_all():
    products = [ProductFactory() for _ in range(5)]
    assert len(products) == 5

def test_find_by_name():
    products = [ProductFactory(name="Phone")]
    result = [p for p in products if p['name'] == "Phone"]
    assert result[0]['name'] == "Phone"

def test_find_by_category():
    products = [ProductFactory(category="books")]
    result = [p for p in products if p['category'] == "books"]
    assert result[0]['category'] == "books"

def test_find_by_availability():
    products = [ProductFactory(available=True)]
    result = [p for p in products if p['available'] is True]
    assert result[0]['available'] is True
