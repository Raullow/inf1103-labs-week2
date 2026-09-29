stock_quantity_total = 0
rejected_entries = 0
file_path = "inventory.txt"
order_arr = []

# Reads inventory.txt and converts data into array
def load_inventory():
    try:
        # Try to create an empty txt file
        with open(file_path, "x", encoding="utf-8") as inventory:
            print("inventory.txt created!")
            print("There are no orders currently.")
            pass
    # If txt file exists - Read it
    except FileExistsError:
        with open(file_path, "r", encoding="utf-8") as inventory:
            orders = inventory.read()

            # Check if txt file is empty If not display data
            if not orders:
                print("There are no orders currently.")
            else:
                print("Current Orders: " + "\n")
                print(orders)
                print("\n")
    except ValueError:
        ("Error")
        

def get_valid_input():
    while True:
        # Product name input check
        product_input = (input("Enter Product Name: "))
        if product_input == "quit":
            return product_input
        try:
            #check if product name entered is a number
            float(product_input)
            add_failed_entry()
            print("Please enter a proper product name. Please try again")
            continue
        except ValueError:
            pass

        while product_input is not None:
            # Quantity input check
            quantity_input = (input("Enter Quantity: "))
            if quantity_input == "quit":
                return quantity_input
            try:
                quantity_input = int(quantity_input)
                break
            except ValueError:
                add_failed_entry()
                print("Invalid input. Please enter a valid integer.")
                continue
        order_arr.append([product_input, quantity_input])
        print(f"{product_input},{quantity_input}")
        return order_arr

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
load_inventory()
# Prompt loop
while True:
    input_value = get_valid_input()

    # Check if user input quit and stops app
    if input_value == "quit":
        if(order_arr):
            save_inventory(order_arr)
        print("Application closed!")
        break
    # Check if return value is array and saves array to txt file
    elif isinstance(input_value, list):
        continue