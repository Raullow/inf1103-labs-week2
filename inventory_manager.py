stock_quantity_total = 0
rejected_entries = 0
file_path = "inventory.json"
order_arr = []

def main():
    print("----------MENU----------\n" 
        "1. Display all products\n"
        "2. Add product\n"
        "3. Update Stock\n"
        "4. Search Product\n"
        "5. Save Inventory\n"
        "6. Exit\n"
        "------------------------\n")

    menu_input = input("Enter option: ")
    if(menu_input == "1"):
        load_inventory()
    elif(menu_input == "2"):
        add_product()
    # elif(menu_input == "3"):

    # elif(menu_input == "4"):

    # elif(menu_input == "5"):

    elif(menu_input == "6"):
        print("Exiting application...")
        exit()
    else:
        print("Invalid option. Please try again.")
        main()
    
def get_valid_input(prompt, validation_fn, error_message):
    #Repeatedly prompts the user for input until the validation function returns True.
    while True:
        user_input = input(prompt).strip()
        if validation_fn(user_input):
            return user_input
        print(f"❌ {error_message}\n")


# --- Define unique validation logic for each of the 4 inputs ---

# 1. Type & Range Check: Must be an integer between 1 and 120
def validate_product_id(product_id):
    quit_application(product_id)
    return product_id


# 2. Length Check: Minimum 8 characters
def validate_product_name(product_name):
    quit_application(product_name)
    return isinstance(product_name, str)

# 3. Format/Character Check: Only letters allowed, cannot be empty
def validate_price(price):
    quit_application(price)
    return price.replace('.', '', 1).isdigit() and float(price) > 0

# 4. Presence/Choice Check: Must match exact options
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
        with open(file_path, "r", encoding="utf-8") as inventory:
            orders = inventory.read()

            # Check if json file is empty If not display data
            if not orders:
                print("There are no orders currently.")
            else:
                print("Current Orders: " + "\n")
                print(orders)
                print("\n")
    except ValueError:
        ("Error")
        

def add_product():

    productId_input = get_valid_input("Enter Product ID: ", validate_product_id, "Product ID already exists or is invalid. Please try again.")
    product_name_input = get_valid_input("Enter Product Name: ", validate_product_name, "Product name is not valid. Please try again.")
    product_price_input = get_valid_input("Enter Product Price: ", validate_price, "Please enter a valid price.")
    product_quantity_input = get_valid_input("Enter Product Quantity: ", validate_quantity, "Please enter a valid quantity.")

    product_arr = [productId_input, product_name_input, product_price_input, product_quantity_input]
    print(f"Product added: {product_arr}")
    print("Product added successfully!")

    return product_arr

def save_inventory(order):
    try:
        with open(file_path, "a", encoding="utf-8") as inventory:
            # inventory.write(str(order))
            print("New Order Added: ")
            for item in order:

                inventory.write(f"{str(item[0])},{str(item[1])} \n")
                print(f"{item[0]}, {item[1]}")

            print("Order successfully saved to " + file_path)
    except ValueError:
        print(f"{file_path} does not exist")


def process_delivery(current_total, new_value):
    current_total += new_value
    print("Added ", new_value, " units. Current inventory: ", current_total)
    return current_total

def calculate_tax(amount):
    amount *= 0.1
    return amount
def generate_report(total_units, failed_entries):
    print("Total units processed: ", total_units)
    print("Total tax of deliveries: ", calculate_tax(total_units))
    print("Number of Failed/Rejected entries: ", failed_entries)

def add_failed_entry():
    global rejected_entries
    rejected_entries += 1

# Initial load inventory
# load_inventory()
# Prompt loop
# while True:
#     input_value = get_valid_input()

#     # Check if user input quit and stops app
#     if input_value == "quit":
#         if(order_arr):
#             save_inventory(order_arr)
#         print("Application closed!")
#         break
#     # Check if return value is array and saves array to txt file
#     elif isinstance(input_value, list):
#         continue
main()