#menu = """
#-----------------------------------
#PRODUCTS INVENTORY APPLICATION
#-----------------------------------
#
#Welcome @s2t2!
#
#There are 20 products in the database.
#
#    operation | description
#    --------- | ------------------
#    'Create'  | Add a new product.
#    'Read'    | Show information about a product.
#    'Update'  | Edit an existing product.
#    'Destroy' | Delete an existing product.
#
#Please select an operation: """ # end of multi- line string
#
#crud_operation = input(menu)
#
#if crud_operation in ["Create", "Read", "Update", "Destroy"]:
#    print("YOU CHOSE", crud_operation.upper())
#else:
#    print("OOPS SORRY. PLEASE TRY AGAIN.")





csv_path = "data/products.csv"

with open(csv_path,'r') as csv:
    output = csv.read()
    print(type(output))
    print(output)
