stock_quantity = 0
stock_quantity_total = 0
rejected_entries = 0

def get_valid_input():
    while True:
        try:
            inventory_input = (input("Enter stock quantity: "))
            try:
                if inventory_input == "quit":
                    return inventory_input
                if int(inventory_input) <= 0:
                    print("Inventory must be greater than 0. Please try again.")
                    continue
                """ if(stock_quantity_total > 500):
                    print("Total stock quantity exceeded 500. Please try again.")
                    break """
                return int(inventory_input)
                
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def process_delivery(current_total, new_value):
    current_total += new_value
    print("Added ", new_value, " units. Current inventory: ", current_total)
    return current_total

def calculate_tax(amount):
    tax = amount * 0.1
    return tax
def generate_report(total_units, failed_entries):
    print("Total units processed: ", total_units)
    print("Number of Failed/Rejected entries: ", failed_entries)
    
print(get_valid_input())
""" 
    while stock_quantity >= 0:
    try:
        inventory_input = (input("Enter stock quantity: "))
        try:
            if inventory_input == "quit":
                print("Total units proccessed: ", stock_quantity_total)
                print("Number of Failled/Rejected entries: ", rejected_entries)
                break
            if int(inventory_input) <= 0:
                print("Inventory must be greater than 0. Please try again.")
                rejected_entries += 1
                continue
            stock_quantity = int(inventory_input)
            stock_quantity_total += stock_quantity
            if(stock_quantity_total > 500):
                print("Total stock quantity exceeded 500. Please try again.")
                break
            print("Added ", stock_quantity, " units. Current inventory: ", stock_quantity_total)
            
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            rejected_entries += 1
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
 """