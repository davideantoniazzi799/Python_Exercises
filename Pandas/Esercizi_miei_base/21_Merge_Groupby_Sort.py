# Create these DataFrames:
#
# customers = {
#   "customer_id": [1, 2, 3, 4],
#   "name": ["Alice", "Bob", "Charlie", "David"],
#   "city": ["Rome", "Milan", "Rome", "Naples"]
# }
#
# orders = {
#   "order_id": [101, 102, 103, 104, 105],
#   "customer_id": [1, 2, 2, 4, 1],
#   "amount": [250, 300, 150, 400, 100]
# }
#
# Then:
# - merge the DataFrames on "customer_id"
# - group by city
# - compute total sales per city
# - sort results by total sales descending
#
# Print the final DataFrame

import pandas as pd

customers = {
    "customer_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "city": ["Rome", "Milan", "Rome", "Naples"]
}

orders = {
    "order_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 2, 4, 1],
    "amount": [250, 300, 150, 400, 100]
}

customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)

merge_df = pd.merge(customers_df, orders_df, how="inner", on="customer_id")
cities_sum_sales = merge_df.groupby("city")["amount"].sum().sort_values(ascending=False)

#final_df = (
#    merge_df
#    .groupby("city", as_index=False)["amount"]
#    .sum()
#    .rename(columns={"amount": "total_sales"})
#    .sort_values("total_sales", ascending=False)
#)

#print(final_df)

print("Total sales per city:")
print(cities_sum_sales)
