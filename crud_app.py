#from IPython import embed
import csv

products_csv = "data/products.csv"

headers = ["id", "name", "aisle", "department", "price"] # for "Further Exploration" use: ["product_id", "product_name", "aisle_id", "aisle_name", "department_id", "department_name", "price"]

products = []

#
# READ PRODUCTS FROM FILE
#

with open(products_csv, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for ordered_dict in reader:
        products.append(dict(ordered_dict))

#
# HANDLE USER INPUT
#

def list_products():
    print("LISTING PRODUCTS HERE")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id]
    if product:
        print("READING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

def create_product():
    print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
    product_id = len(products) # auto-increment product identifiers
    product = {"id": product_id}
    other_headers = [header for header in headers if header != "id"] # don't prompt the user for the product_id
    for header in other_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT HERE", product)

def update_product():
    print("UPDATING PRODUCT HERE")

def destroy_product():
    print("DESTROYING PRODUCT HERE")

menu = """
-----------------------------------
PRODUCTS APPLICATION
-----------------------------------

Welcome {0}!

There are {1} products in the database.

    operation | description
    --------- | ------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.

Please select an operation: """.format("@s2t2", len(products)) # end of multi- line string. also using string interpolation

crud_operation = input(menu)

if crud_operation.title() == "List":
    list_products()
elif crud_operation.title() == "Show":
    show_product()
elif crud_operation.title() == "Create":
    create_product()
elif crud_operation.title() == "Update":
    update_product()
elif crud_operation.title() == "Destroy":
    destroy_product()
else:
    print("OOPS SORRY. PLEASE TRY AGAIN.")

#
# WRITE PRODUCTS TO FILE
#

with open(products_csv, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()

    for product in products:
        writer.writerow(product)
