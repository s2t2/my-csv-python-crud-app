from my_app.crud_app import *

def test_get_product_id():
    read_products_from_file("tests/example_products.csv")
    assert get_product_id(products[0]) == 3

def test_auto_incremented_id():
    read_products_from_file("tests/example_products.csv")
    assert auto_incremented_id() == 201
