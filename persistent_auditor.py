stock_quantity_total = 0
rejected_entries = 0
file_path = "inventory.txt"
default_serial_no = 1000

# Reads inventory.txt and converts data into array
def load_inventory():
    try:
        with open(file_path, "x", encoding="utf-8") as inventory:
            pass
    except FileExistsError:
        with open(file_path, "r", encoding="utf-8") as inventory:
            print("Current Orders: " + "\n")
            print(inventory.read())
            print("\n")
        

def get_valid_input():
    order_arr = []
    while True:

        # Product name input check
        product_input = (input("Enter Product Name: "))
        if product_input == "quit":
            return product_input
        try:
            #check if product name entered is a number
            float(product_input)
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
                print("Invalid input. Please enter a valid integer.")
                continue
        order_arr.append(product_input)
        order_arr.append(str(quantity_input))
        return order_arr

def save_inventory(order):
    try:
        with open(file_path, "a", encoding="utf-8") as inventory:
            order_str = ', '.join(order)
            inventory.write(order_str + "\n")

            print("\n")
            print("New Order Added: " + "\n" + order_str)
            print("\n")
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
        print("Application closed!")
        break
    # Check if return value is array and saves array to txt file
    elif isinstance(input_value, list):
        save_inventory(input_value)
        continue

# generate_report(stock_quantity_total, rejected_entries)