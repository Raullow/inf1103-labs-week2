import json

file_path = "inventory.json"
current_order = []

def main():
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
            load_inventory()
        elif(menu_input == "2"):
            add_product()
        elif(menu_input == "3"):
            print("\nUpdate Stock")
            update_stock()
        elif(menu_input == "4"):
            print("\nSearch Product")
           
            search_product()
        elif(menu_input == "5"):
            save_inventory(current_order)
            print("Saving inventory...\n")

        elif(menu_input == "6"):
            print("Saving inventory before exit...\n")
            save_inventory(current_order)
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

def quit_application(input):
    if input == "quit":
        print("Closing application...")
        exit()
    else:
        return

# Reads inventory.json and converts data into array
def load_inventory():
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

                # Check if json file is empty If not display data
                if not products["inventory"]:
                    print("There are no products currently.")
                else:
                    print("Current Inventory\n"
                    "-----------------")
                    for product in products["inventory"]:
                        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']} | Quantity: {product['quantity']}")
                    print("------------------")
                    return
        except json.JSONDecodeError:
            print("There are no products currently.")
            return
    except ValueError:
        print("Error")
        return

def add_product():

    productId_input = get_valid_input("Enter Product ID (eg: P001): ", validate_product_id, "Product ID already exists or is invalid. Please try again.")
    product_name_input = get_valid_input("Enter Product Name: ", validate_product_name, "Product name is not valid. Please try again.")
    product_price_input = get_valid_input("Enter Product Price: ", validate_price, "Please enter a valid price.")
    product_quantity_input = get_valid_input("Enter Product Quantity: ", validate_quantity, "Please enter a valid quantity.")

    product_obj = {
        "id": productId_input,
        "name": product_name_input,
        "price": product_price_input,
        "quantity": product_quantity_input
    }

    current_order.append(product_obj)
    print("Inventory saved successfully to " + file_path + ".\n")
    return product_obj

def update_stock():
    product_id_input = get_valid_input("Enter Product ID to update stock: ", validate_product_id, "Product ID not found. Please try again.")
    try:
        with open(file_path, "r") as inventory:
            products = json.load(inventory)
    except json.JSONDecodeError:
        print("Inventory is empty. Cannot update stock.")
        return

    for product in products["inventory"]:
        if product["id"] == product_id_input:
            print(f"\nProduct found: \n Name: {product['name']} \n Current Stock: {product['quantity']}")
            new_quantity_input = get_valid_input("Enter new stock quantity: ", validate_quantity, "Please enter a valid quantity.")
            product["quantity"] = new_quantity_input
            break
    else:
        print("Product ID not found.")
        return

    with open(file_path, "w") as file:
        json.dump(products, file, indent=4)
    print(f"\nStock for Product ID {product_id_input} updated to {new_quantity_input}.")

def search_product():
    product_id_input = get_valid_input("Enter Product ID to search: ", validate_product_id, "Product ID not found. Please try again.")
    try:
        with open(file_path, "r") as inventory:
            products = json.load(inventory)
    except json.JSONDecodeError:
        print("Inventory is empty. Cannot search for products.")
        return

    for product in products["inventory"]:
        if product["id"] == product_id_input:
            print("\nProduct found: \n" +
                "----------------------------\n" +
                f"ID: {product['id']} \n" +
                f"Name: {product['name']} \n" +
                f"Price: ${product['price']} \n" +
                f"Quantity: {product['quantity']} \n" +
                "----------------------------\n")
            return
    print("Product ID not found.")

def save_inventory(order):
    if order:
        try:
            with open(file_path, "r") as inventory:
                products = json.load(inventory)
        except json.JSONDecodeError:
            products = {"inventory": []}

        for item in order:
            products["inventory"].append(item)

        with open(file_path, "w") as file:
            json.dump(products, file, indent=4)
        print("Products added successfully!")
        current_order.clear()  # Clear the current order after saving
        return
    elif not order:
        print("No products to save.")

# run the main function when the script is executed
main()