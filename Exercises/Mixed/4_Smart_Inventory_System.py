# ======================
# EXERCISE 4 — Smart Inventory System
# ======================
#
# Create a class Inventory:
#
# Store items as a dictionary:
# {
#   "item_name": {
#       "price": float,
#       "quantity": int
#   }
# }
#
# Methods:
# - add_item(name, price, quantity)
# - remove_item(name)
# - total_value() → uses NumPy to compute total inventory value
# - low_stock(threshold=5) → returns items below threshold
# - to_dataframe()
#
# Print:
# - Full inventory table
# - Total inventory value
# - Low stock items

import pandas as pd
import numpy as np

THRESHOLD = 5

class Inventory:
    def __init__(self):
        self.items_dict = {}

    #ADDING ITEMS
    def add_item(self, name, price, quantity):
        if name in self.items_dict:
            raise KeyError(f"Item '{name}' already exists")

        try:
            price = float(price)
            quantity = int(quantity)
        except (ValueError, TypeError):
            raise TypeError("Price must be a number and quantity must be an integer")

        if price <= 0:
            raise ValueError("Price must be positive")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.items_dict[name] = {
            "price": price,
            "quantity": quantity
        }

    #REMOVE ITEMS
    def remove_item(self, name):
        if name in self.items_dict:
            del self.items_dict[name]
        else:
            raise KeyError(f"Item '{name}' not found in inventory")
    
    #TO DATAFRAME
    def to_dataframe(self):
        df = pd.DataFrame(self.items_dict)
        return df.transpose()
    
    #TOTAL INVENTORY VALUE
    def total_value(self, df):
        return np.sum(df["price"]*df["quantity"])
    
    #LOW STOCK
    def low_stock(self, df):
        filtered = df[df["quantity"] <= THRESHOLD]

        if filtered.empty:
            return "No items below threshold"

        return filtered
 
inventory = Inventory()
inventory.add_item(name="tomato", price = 2.49, quantity=2)
inventory.add_item(name="carrot", price = 0.99, quantity=5)
inventory.add_item(name="milk", price = 0.89, quantity=15)
#inventory.remove_item(name = "carrot")    

full_inventory_items = inventory.to_dataframe()
total_inventory_value = inventory.total_value(df = full_inventory_items)
low_stock_items = inventory.low_stock(df = full_inventory_items)

print("Full inventory:")
print(full_inventory_items)

print("\nTotal inventory value: € ")
print(total_inventory_value)

print(f"\nLow stock items(<={THRESHOLD}):")
print(low_stock_items)