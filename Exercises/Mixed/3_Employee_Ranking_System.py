# ======================
# EXERCISE 3 — Employee Ranking System
# ======================
#
# Create a class EmployeeRanker that:
# - Accepts two lists of dictionaries:
#
# employees = [
#   {"emp_id": 1, "name": "Alice"},
#   {"emp_id": 2, "name": "Bob"},
#   {"emp_id": 3, "name": "Charlie"}
# ]
#
# sales = [
#   {"emp_id": 1, "amount": 200},
#   {"emp_id": 2, "amount": 300},
#   {"emp_id": 2, "amount": 150},
#   {"emp_id": 3, "amount": 400}
# ]
#
# Methods:
# - merge_data()
# - total_sales_per_employee()
# - add_bonus(percent=0.1)
# - rank_employees()
#
# Print a final ranked DataFrame

import pandas as pd

PERCENT = 0.1

class EmployeeRanker:
    def __init__(self):
        self.employees = []
        self.sales = []
        df_employees = pd.DataFrame(self.employees)
        df_sales = pd.DataFrame(self.sales)

    #Adding the employees and sales list
    def add_employees_sales_list(self, employees_list, sales_list):
        self.employees.extend(employees_list)
        self.sales.extend(sales_list)

        self.df_employees = pd.DataFrame(self.employees)
        self.df_sales = pd.DataFrame(self.sales)

    #Merging DataFrame
    def merge_data(self):
        df_employees_sales = pd.merge(self.df_employees, self.df_sales, on= "emp_id", how= "inner")
        return df_employees_sales
    
    #Total sales per employee
    def total_sales_per_employee(self, df):
        return (df.groupby("name", as_index=False).agg(amount=("amount", "sum")))
    
    #Adding bonus
    def add_bonus(self, df):
        df["Bonus"] = df["amount"] * PERCENT
        return df
    
    #Ranking employee
    def rank_employees(self, df):
        df["rank"] = df["amount"].rank(method = "dense", ascending=False)
        return df


employees = [
    {"emp_id": 1, "name": "Alice"},
    {"emp_id": 2, "name": "Bob"},
    {"emp_id": 3, "name": "Charlie"}
]

sales = [
    {"emp_id": 1, "amount": 200},
    {"emp_id": 2, "amount": 300},
    {"emp_id": 2, "amount": 150},
    {"emp_id": 3, "amount": 400}
]

#Creating the object
employee_ranker = EmployeeRanker()

#Add lists to dataframe   
employee_ranker.add_employees_sales_list(employees_list=employees, sales_list=sales)

#Merging
df_merged = employee_ranker.merge_data()

#Total sales per employee
df_sales_employee = employee_ranker.total_sales_per_employee(df = df_merged)

#Adding bonus 
df_sales_employee = employee_ranker.add_bonus(df = df_sales_employee)

#Rank empployees
df_sales_employee = employee_ranker.rank_employees(df = df_sales_employee)

print("Final employees rank by amount of sales:")
print(df_sales_employee.sort_values("rank", ascending=True))