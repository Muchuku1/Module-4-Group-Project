# Inventory Management System

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture & OOP Desgin](#architecture--oop-design)
- [Setup Instruction](#setup-instructions)
- [Usage](#usage)
- [Authors](#authors)
- [Contacts](#contacts)
- [License](#mit-license)

## Overview

A simple command-line inventory management system for a supermarket, written in Python. Products are managed through an Inventory class and saved to a JSON file, so stock data persists between runs.

## Features

- **Role-based Menu Options:** Dedicated actions for Store Managers and Customer Service.
- **Product Registration:** Add new items with ID, name, price, and initial quantity.
- **Restocking:** Quickly increase stock levels for existing items.
- **Sales Monitoring:** Deduct sold quantities from the inventory (with stock limit checking).
- **Search & Filter:** Search for items by name or ID, and view a list of all out-of-stock items.
- **Save Data:** Inventory is saved to `data/inventory.json` automatically after every action.

## Architecture & OOP Design

The project follows the principles of Object-Oriented Programming (OOP) and separation of concerns:

- **`main.py`**: The entry point. It simply calls the CLI.
- **`src/cli.py`**: Handles all user input, menu rendering, and error catching (e.g., catching `ValueError` if a user types letters instead of numbers).
- **`src/inventory.py`**: The core logic controller. It manages the dictionary of products, handles file I/O (JSON load/save), and executes business rules (e.g., preventing negative stock).
- **`src/product.py`**: A simple data model class representing a single product entity.

## Setup Instructions

1. **Clone the repository:**

```bash
git clone git@github.com:Muchuku1/Module-4-Group-Project.git
cd Module-4-Group-Project
```

2. **Ensure your using Python version 3.8+**:

```bash
python3 --version
```

3. **Run the application**

```bash
python3 main.py
```

## Usage

When you run python main.py, you will be greeted with the interactive menu:

```text
========================================
      INVENTORY MANAGEMENT SYSTEM       
========================================
1. Register New Product (Store Manager)
2. Restock Stock Levels (Store Manager)
3. Monitor Sales & Update Sold Items (Customer Service)
4. Search Through Inventory Items
5. View 'Out of Stock' Items
6. View All Inventory Products
7. Save Inventory 
8. Exit

Enter your choice (1-8):
```

### Example Workflow

Example Workflow:

- Register a product: Choose 1, enter ID A001, name Milk, price 2.50, quantity 50. The product is instantly saved to data/inventory.json.

- Sell a product: Choose 3, enter ID A001, quantity 5. The system updates the stock to 45.

- Check low stock: Choose 5 to see a list of items that need restocking.

## Authors

- Cliff Mwamburi
- Victor Kipkemboi
- Victor Wasunna

## Contacts

- <muchukucliff@gmail.com>
- <rickvick142@gmail.com>
- <wvictoronyango@gmail.com>

## MIT License

Copyright © 2026 The Binary Brigade

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.