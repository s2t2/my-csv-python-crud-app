from app.products_app import *

import pytest # for error-raising function .raise

#
# Tests for read_products_from_file()
#

def test_read_products_from_file():
    products = read_products_from_file("tests/example_products.csv")
    assert len(products) == 8
    assert products[0]["name"] == "Robust Golden Unsweetened Oolong Tea"

#
# Tests for map_id()
#

def test_map_id():
    products = read_products_from_file("tests/example_products.csv")
    assert map_id(products[0]) == 3

#
# Tests for auto_increment_id()
#

def test_auto_increment_id():
    products = read_products_from_file("tests/example_products.csv")
    assert auto_increment_id(products) == 201

def test_auto_increment_id_given_empty_inventory():
    products = read_products_from_file("tests/empty_products.csv")
    assert auto_increment_id(products) == 1

def test_auto_increment_id_given_reordered_inventory():
    products = read_products_from_file("tests/reordered_products.csv")
    assert auto_increment_id(products) == 201

#
# Tests for user_inputtable_headers()
#

def test_read_products_from_file():
    assert user_inputtable_headers() == ["name","aisle", "department","price"]

#
# Tests for lookup_product()
#

def test_lookup_product():
    products = read_products_from_file("tests/example_products.csv")
    product_id = 15
    product = lookup_product(product_id, products)
    assert int(product["id"]) == product_id
    assert product["name"] == "Overnight Diapers Size 6"

def test_lookup_product_given_reordered_inventory():
    products = read_products_from_file("tests/reordered_products.csv")
    product_id = 15
    product = lookup_product(product_id, products)
    assert int(product["id"]) == product_id
    assert product["name"] == "Overnight Diapers Size 6"

def test_lookup_product_given_empty_inventory():
    products = read_products_from_file("tests/empty_products.csv")
    with pytest.raises(IndexError):
        lookup_product(15, products) # should raise... IndexError: list index out of range

def test_lookup_product_not_found():
    products = read_products_from_file("tests/example_products.csv")
    with pytest.raises(IndexError):
        lookup_product(12345678, products) # should raise... IndexError: list index out of range

#
# Tests for list_products()
#

def test_list_products():
    products = read_products_from_file("tests/example_products.csv")
    assert len(products) == 8

def test_list_products_in_empty_inventory():
    products = read_products_from_file("tests/empty_products.csv")
    assert len(products) == 0
