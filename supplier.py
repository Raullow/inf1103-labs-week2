class Supplier:
    def __init__(self, supplier_id: int, name: str, contact_email: str):
        self.supplier_id: int = supplier_id
        self.name: str = name
        self.contact_email: str = contact_email

    def display_information(self):
        print(f"Supplier ID: {self.supplier_id}")
        print(f"Name: {self.name}")
        print(f"Contact Email: {self.contact_email}")