from src.models import Product

class Inventory:
    def __init__(self):
        # Initial sample products for demonstration
        self.products = {
            "101": Product("101", "Maize Flour (2kg)", 180.0, 15),
            "102": Product("102", "Cooking Oil (1L)", 350.0, 0),
            "103": Product("103", "Milk (500ml)", 60.0, 8)
        }

    def register_product(self, product_id, name, price, quantity):
        """Register a new product into the supermarket inventory[cite: 1]."""
        if product_id in self.products:
            return False, "Product ID already exists."
        self.products[product_id] = Product(product_id, name, price, quantity)
        return True, "Product registered successfully."

    def restock_product(self, product_id, amount):
        """Restock low-level stock items (Store Manager feature)[cite: 1, 2]."""
        if product_id not in self.products:
            return False, "Product not found."
        self.products[product_id].quantity += int(amount)
        return True, f"Successfully restocked. New quantity: {self.products[product_id].quantity}"

    def update_sold_items(self, product_id, amount):
        """Monitor sales and update inventory on sold items (Customer Service feature)[cite: 1, 2]."""
        if product_id not in self.products:
            return False, "Product not found."
        product = self.products[product_id]
        if product.quantity < int(amount):
            return False, f"Not enough stock available! Current stock: {product.quantity}"
        product.quantity -= int(amount)
        return True, f"Sale recorded. Remaining quantity: {product.quantity}"

    def search_items(self, query):
        """Search through inventory items by name or ID[cite: 1]."""
        query = query.lower()
        results = [p for p in self.products.values() if query in p.name.lower() or query in p.product_id]
        return results

    def get_out_of_stock(self):
        """View 'out of stock' items[cite: 1]."""
        return [p for p in self.products.values() if p.quantity == 0]

    def get_all_products(self):
        return list(self.products.values())