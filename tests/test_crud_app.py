from app.products_app import *

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

#
# Tests for read_products_from_file()
#

def test_read_products_from_file():
    products = read_products_from_file("tests/example_products.csv")
    assert len(products) == 8
    assert products[0]["name"] == "Robust Golden Unsweetened Oolong Tea"
