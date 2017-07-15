from app.products_app import *

def test_map_id():
    read_products_from_file("tests/example_products.csv")
    assert map_id(products[0]) == 3

def test_auto_incremented_id():
    read_products_from_file("tests/example_products.csv")
    assert auto_incremented_id() == 201
