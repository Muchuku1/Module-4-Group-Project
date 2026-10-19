from src.inventory import Inventory

def run_cli():
    inventory = Inventory()
    
    while True:
        print("\n========================================")
        print("      INVENTORY MANAGEMENT SYSTEM       ")
        print("========================================")
        print("1. Register New Product (Store Manager)[cite: 1, 2]")
        print("2. Restock Stock Levels (Store Manager)[cite: 1, 2]")
        print("3. Monitor Sales & Update Sold Items (Customer Service)[cite: 1, 2]")
        print("4. Search Through Inventory Items[cite: 1]")
        print("5. View 'Out of Stock' Items[cite: 1]")
        print("6. View All Inventory Products")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            pid = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            try:
                price = float(input("Enter Price: "))
                qty = int(input("Enter Initial Quantity: "))
                success, msg = inventory.register_product(pid, name, price, qty)
                print(f"\n[INFO] {msg}")
            except ValueError:
                print("\n[ERROR] Invalid price or quantity format.")
                
        elif choice == "2":
            pid = input("Enter Product ID to restock: ").strip()
            try:
                qty = int(input("Enter quantity to add: "))
                success, msg = inventory.restock_product(pid, qty)
                print(f"\n[INFO] {msg}")
            except ValueError:
                print("\n[ERROR] Invalid quantity format.")
                
        elif choice == "3":
            pid = input("Enter Product ID sold: ").strip()
            try:
                qty = int(input("Enter quantity sold: "))
                success, msg = inventory.update_sold_items(pid, qty)
                print(f"\n[INFO] {msg}")
            except ValueError:
                print("\n[ERROR] Invalid quantity format.")
                
        elif choice == "4":
            query = input("Enter search keyword (Name or ID): ").strip()
            results = inventory.search_items(query)
            if results:
                print("\n--- Search Results ---")
                for p in results:
                    print(f"ID: {p.product_id} | Name: {p.name} | Price: {p.price} | Qty: {p.quantity}")
            else:
                print("\n[INFO] No matching products found.")
                
        elif choice == "5":
            out_of_stock = inventory.get_out_of_stock()
            if out_of_stock:
                print("\n--- Out of Stock Items ---")
                for p in out_of_stock:
                    print(f"ID: {p.product_id} | Name: {p.name}")
            else:
                print("\n[INFO] Great news! No items are currently out of stock.")
                
        elif choice == "6":
            all_p = inventory.get_all_products()
            print("\n--- Current Supermarket Inventory ---")
            for p in all_p:
                print(f"ID: {p.product_id} | Name: {p.name} | Price: {p.price} | Qty: {p.quantity}")
                
        elif choice == "7":
            print("\nExiting Inventory Management System. Goodbye!")
            break
        else:
            print("\n[ERROR] Invalid choice. Please select an option between 1 and 7.")