#from IPython import embed

menu = """
-----------------------------------
PRODUCTS INVENTORY APPLICATION
-----------------------------------

Welcome @s2t2!

There are 20 products in the database.

    operation | description
    --------- | ------------------
    'Create'  | Add a new product.
    'Read'    | Show information about a product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.

Please select an operation: """ # end of multi- line string

crud_operation = input(menu)

def create_product():
    print("CREATING PRODUCT HERE")

def read_product():
    print("READING PRODUCT HERE")

def update_product():
    print("UPDATING PRODUCT HERE")

def destroy_product():
    print("DESTROYING PRODUCT HERE")

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

#csv_path = "data/products.csv"
#with open(csv_path,'r') as csv:
#    output = csv.read()
#    print(type(output))
#    print(output)


#import csv
#
#products_csv = "data/products.csv"
#
#with open(products_csv, 'r') as csv_file:
#    rows = csv.reader(csv_file)
#    print(type(rows))
#    #print(len(list(rows)))
#    for row in rows:
#        print(type(row))
#        print(row)


import csv

#products_csv = "data/products.csv"
#
#with open(products_csv, 'r') as csv_file:
#    reader = csv.DictReader(csv_file) # or if your CSV doesn't have headers use... reader = csv.reader(csv_file)
#    for row in reader:
#        if reader.line_num == 2: print(list(row.keys()))
#        print(row["product_id"])



teams = [
    {"city": "New York", "name": "Yankees"},
    {"city": "New York", "name": "Mets"},
    {"city": "Boston", "name": "Red Sox"},
    {"city": "New Haven", "name": "Ravens"}
]

teams_csv = "data/teams.csv"

with open(teams_csv, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader()

    for team in teams:
        writer.writerow(team)
