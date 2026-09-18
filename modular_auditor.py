stock_quantity_total = 0
rejected_entries = 0

def get_valid_input():
    while True:
        inventory_input = (input("Enter stock quantity: "))
        if inventory_input == "quit":
            return inventory_input
        try:
            inventory_input = int(inventory_input)
            if int(inventory_input) <= 0:
                add_failed_entry()
                print("Inventory must be greater than 0. Please try again.")
            elif int(inventory_input) + stock_quantity_total > 500:
                add_failed_entry()
                print("Total stock quantity exceeded 500. Please try again.")
            else:
                return inventory_input
        except ValueError:
            add_failed_entry()
            print("Invalid input. Please enter a valid integer.")

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

while True:
    input_value = get_valid_input()
    if input_value == "quit":
        break

    stock_quantity_total = process_delivery(stock_quantity_total, input_value)
    print("Tax for the current delivery: ", calculate_tax(stock_quantity_total))
generate_report(stock_quantity_total, rejected_entries)