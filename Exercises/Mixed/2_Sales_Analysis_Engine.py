# ======================
# EXERCISE 2 — Sales Analysis Engine
# ======================
#
# Create a class SalesAnalyzer that:
# - Accepts a list of dictionaries representing orders:
#     {
#       "order_id": int,
#       "city": str,
#       "date": "YYYY-MM-DD",
#       "amount": float
#     }
#
# Methods:
# - to_dataframe()
# - monthly_sales() → returns total sales per month
# - city_performance() → returns total + average sales per city
# - top_orders(n=3) → returns the top N highest orders
#
# Use:
# - Pandas for grouping and datetime
# - NumPy for math and ranking logic

import pandas as pd
import numpy as np

class SalesAnalyzer:
    def __init__(self):
        #list of orders
        self.orders = []
        self.df = pd.DataFrame(self.orders)
    
    #Adding the order to the list
    def add_order(self, order_id, city, date, amount):

        if order_id < 1:
            raise ValueError("Order id must be positive")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if any(order["order_id"] == order_id for order in self.orders):
            raise ValueError("Order id already present")
        
        new_order = {
        "order_id": order_id,
        "city": city,
        "date": date,
        "amount": amount
        }
        
        self.orders.append(new_order)
        
        self.df = pd.DataFrame(self.orders)
    
    #Calculating monthly sales
    def monthly_sales(self, month):
        self.df["date"] = pd.to_datetime(self.df["date"])
        filtered = self.df[self.df["date"].dt.month == month]

        if not 1 <= month <= 12:
            raise ValueError("The value must be between 1 and 12")
        
        if filtered.empty:
            return "No sales for the selected month"

        return filtered
    
    #City performance
    def city_performance(self):
        result = self.df.groupby("city").agg(total_sales = ("amount", "sum"), average_sales = ("amount", "mean"))
        return result
    
    #Top N orders
    def top_orders(self, n):

        if n > len(self.df):
            raise IndexError("The DataFrame is too small.")

        return self.df.nlargest(n, "amount").sort_values("amount")

#Creating the object
salesAnalyzer = SalesAnalyzer()

#Creating the order:
salesAnalyzer.add_order(order_id=1, city="Rome", date = "2024-06-23", amount = 100)
salesAnalyzer.add_order(order_id=2, city="Rome", date = "2024-07-13", amount = 150)

#June sales
month = 6
monthly_sales_june = salesAnalyzer.monthly_sales(month=month)

#City sales
city_sales = salesAnalyzer.city_performance()

#top_orders
n = 1
top_orders = salesAnalyzer.top_orders(n)

print(f"Sales of {month}:")
print(monthly_sales_june)

print("Total and average sale for city:")
print(city_sales)

print(f"Top {n} sales:")
print(top_orders)