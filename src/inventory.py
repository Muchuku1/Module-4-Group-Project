import json
import os
from src.product import Product

class Inventory:
    def __init__(self, filepath="./data/inventory.json"):
        self.filepath = filepath
        self.products = {}
        self.load()

    def load(self):
        if os.path.exists(self.filepath) and os.path.getsize(self.filepath) > 0:
            with open(self.filepath, "r") as f:
                data = json.load(f)
            self.products = {
                pid: Product(pid, p["name"], p["price"], p["quantity"])
                for pid, p in data.items()
            }

    def save(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        data = {
            pid: {"name": p.name, "price": p.price, "quantity": p.quantity}
            for pid, p in self.products.items()
        }
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)

    def register_product(self, product_id, name, price, quantity):
        if product_id in self.products:
            return False, "Product ID already exists."
        self.products[product_id] = Product(product_id, name, price, quantity)
        self.save()
        return True, "Product registered successfully."

    def restock_product(self, product_id, amount):
        if product_id not in self.products:
            return False, "Product not found."
        self.products[product_id].quantity += int(amount)
        self.save()
        return True, f"Successfully restocked. New quantity: {self.products[product_id].quantity}"

    def update_sold_items(self, product_id, amount):
        if product_id not in self.products:
            return False, "Product not found."
        product = self.products[product_id]
        if product.quantity < int(amount):
            return False, f"Not enough stock available! Current stock: {product.quantity}"
        product.quantity -= int(amount)
        self.save()
        return True, f"Sale recorded. Remaining quantity: {product.quantity}"

    def search_items(self, query):
        query = query.lower()
        return [p for p in self.products.values()
                if query in p.name.lower() or query in p.product_id]

    def get_out_of_stock(self):
        return [p for p in self.products.values() if p.quantity == 0]

    def get_all_products(self):
        return list(self.products.values())