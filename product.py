class Product:
    def __init__(self, product_id, name, price, stock):
            self.product_id = product_id
            self.name = name
            self.price = float(price)
            self.stock = int(stock)

            def update_stock(self, new_stock):
                if new_stock < 0 or new_stock.isdigit() == False:
                    print("Stock cannot be negative. Please enter a valid stock quantity.")
                    return
                self.stock = int(new_stock)
                print(f"\nStock updated to {self.stock}.")

            def display_information(self):
                print("\nProduct found: \n" +
                    "----------------------------\n" +
                    f"ID: {self.product_id} \n" +
                    f"Name: {self.name} \n" +
                    f"Price: ${self.price:.2f} \n" +
                    f"Stock: {self.stock} \n" +
                    "----------------------------\n")