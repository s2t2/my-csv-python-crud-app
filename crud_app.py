#from IPython import embed
import csv

products_csv = "data/products.csv"

headers = [
  "product_id",
  "product_name",
  "aisle_id",
  "aisle_name",
  "department_id",
  "department_name",
  "price"
]

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

def create_product():
    print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
    product = {}
    for header in headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT HERE")

def read_product():
    print("READING PRODUCT HERE")

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
    'Create'  | Add a new product.
    'Read'    | Show information about a product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.

Please select an operation: """.format("@s2t2", len(products)) # end of multi- line string. also using string interpolation

crud_operation = input(menu)

if crud_operation.title() == "Create":
    create_product()
elif crud_operation.title() == "Read":
    read_product()
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
