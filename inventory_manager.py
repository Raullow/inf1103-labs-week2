import json
from product import Product 
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

file_path = "inventory.json"

def main():
    products = []
    inventory_cls = Inventory()
    load_inventory(inventory_cls)

    print("----------MENU----------\n" 
        "1. Display all products\n"
        "2. Add product\n"
        "3. Update Stock\n"
        "4. Search Product\n"
        "5. Save Inventory\n"
        "6. Exit\n"
        "------------------------\n")

    while True:
        menu_input = input("Enter option: ")
        quit_application(menu_input)
        if(menu_input == "1"):
            inventory_cls.display_all()
        elif(menu_input == "2"):
            add_product(inventory_cls)
        elif(menu_input == "3"):
            print("\nUpdate Stock")
            update_stock(inventory_cls)
        elif(menu_input == "4"):
            print("\nSearch Product")
           
            search_product(inventory_cls)
        elif(menu_input == "5"):
            save_inventory(inventory_cls)
            print("Saving inventory...\n")

        elif(menu_input == "6"):
            print("Saving inventory before exit...\n")
            save_inventory(inventory_cls)
            print("\n Thank you for using the Inventory Management System. Goodbye! \n Program terminated.")
            exit()
        else:
            print("Invalid option. Please try again.")
            main()

#validation function to get valid input from user
def get_valid_input(prompt, validation_fn, error_message):
    while True:
        user_input = input(prompt).strip()
        if validation_fn(user_input):
            return user_input
        print(f" {error_message}\n")



# validation functions for product attributes

#check if product ID is valid (4 characters, starts with 'P', followed by 3 digits)
def validate_product_id(product_id):
    quit_application(product_id)
    if len(product_id) == 4 and product_id.startswith('P') and product_id[1:].isdigit():
        return product_id

# check if product name is a string
def validate_product_name(product_name):
    quit_application(product_name)
    return isinstance(product_name, str)

# Check if price input is a positive number (float or int)
def validate_price(price):
    quit_application(price)
    return price.replace('.', '', 1).isdigit() and float(price) > 0

# Check if quantity input is a positive integer
def validate_quantity(quantity):
    quit_application(quantity)
    return quantity.isdigit() and int(quantity) > 0

# Check if weight input is a positive number (float or int)
def validate_weight(weight):
    quit_application(weight)
    return weight.replace('.', '', 1).isdigit() and float(weight) > 0

# Check if download size input is a positive number (float or int)
def validate_download_size(download_size):
    quit_application(download_size)
    return download_size.replace('.', '', 1).isdigit() and float(download_size) > 0

def validate_product_type(product_type):
    quit_application(product_type)
    return product_type in ["1", "2"]

def quit_application(input):
    if input == "quit":
        print("Closing application...")
        exit()
    else:
        return

# Reads inventory.json and converts data into array
def load_inventory(inventory_cls):
    try:
        # Try to create an empty json file
        with open(file_path, "x", encoding="utf-8") as inventory:
            print("inventory.json created!")
            print("There are no orders currently.")
            pass
    # If json file exists - Read it
    except FileExistsError:
        try:
            with open(file_path, "r", encoding="utf-8") as inventory:
                products = json.load(inventory)

                for product in products["inventory"]:
                    if(product["type"] == "Physical"):
                        inventory_cls.add_product(PhysicalProduct(product["id"], product["name"], product["price"], product["quantity"], product["weight"]))
                    elif(product["type"] == "Digital"):
                        inventory_cls.add_product(DigitalProduct(product["id"], product["name"], product["price"], product["quantity"], product["download_size"]))
        except json.JSONDecodeError:
            print("There are no products currently.")
            return
    except ValueError:
        print("Error")
        return

def add_product(inventory_cls):

    product_type_input = get_valid_input("Enter Product Type: \n1. Physical\n2. Digital\nEnter your choice (1 or 2): ", validate_product_type, "Please enter '1' for Physical or '2' for Digital.")
    productId_input = get_valid_input("Enter Product ID (eg: P001): ", validate_product_id, "Product ID already exists or is invalid. Please try again.")
    product_name_input = get_valid_input("Enter Product Name: ", validate_product_name, "Product name is not valid. Please try again.")
    product_price_input = get_valid_input("Enter Product Price: ", validate_price, "Please enter a valid price.")
    product_quantity_input = get_valid_input("Enter Product Quantity: ", validate_quantity, "Please enter a valid quantity.")
    
    if product_type_input == "1":
        product_weight_input = get_valid_input("Enter Product Weight (kg): ", validate_weight, "Please enter a valid weight.")
        product = PhysicalProduct(productId_input, product_name_input, product_price_input, product_quantity_input, product_weight_input)
    elif product_type_input == "2":
        product_download_size_input = get_valid_input("Enter Product Download Size (MB): ", validate_download_size, "Please enter a valid download size.")
        product = DigitalProduct(productId_input, product_name_input, product_price_input, product_quantity_input, product_download_size_input)

    if inventory_cls.add_product(product):
        print("Product added. Choose 'Save Inventory' to write it to file.\n")
    else:
        print("Product ID already exists. Product not added.\n")


def update_stock(inventory_cls):
    product_id = get_valid_input("Enter Product ID to update stock: ", validate_product_id,
                                 "Invalid Product ID. Must look like P001.")
    product = inventory_cls.search_product(product_id)
    if product is None:
        print("Product ID not found.")
        return
 
    print("\nProduct found:")
    product.display_information()
    new_quantity = get_valid_input("Enter new stock quantity: ", validate_quantity,
                                   "Please enter a valid quantity.")
    product.update_stock(new_quantity)
    print(f"\nStock for Product ID {product_id} updated to {product.stock}.")
    

def search_product(inventory_cls):
    product_id_input = get_valid_input("Enter Product ID to search: ", validate_product_id, "Product ID not found. Please try again.")
    product = inventory_cls.search_product(product_id_input)
    if product is None:
        print("Product ID not found.")
    else:
        print("\nProduct found:")
        product.display_information()
        product.get_fulfillment_info()
        if(isinstance(product, PhysicalProduct)):
            print(f"Estimated shipping cost: ${product.calculate_shipping_cost():.2f}")

def save_inventory(inventory_cls):
    orders = []
    if inventory_cls.get_products():
        for product in inventory_cls.get_products():
            if isinstance(product, PhysicalProduct):
                orders.append({
                    "id": product.product_id,
                    "type": product.type,
                    "name": product.name,
                    "price": product.price,
                    "quantity": product.stock,
                    "weight": product.weight
                })
            elif isinstance(product, DigitalProduct):
                orders.append({
                    "id": product.product_id,
                    "type": product.type,
                    "name": product.name,
                    "price": product.price,
                    "quantity": product.stock,
                    "download_size": product.download_size
                })
        with open(file_path, "w") as file:
            json.dump({"inventory": orders}, file, indent=4)
        print("Products added successfully!")
        return
    elif not orders:
        print("No products to save.")

# run the main function when the script is executed
main()