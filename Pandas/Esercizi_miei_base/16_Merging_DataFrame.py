# Create two DataFrames:
# customers = {
#   "customer_id": [1, 2, 3, 4],
#   "name": ["Alice", "Bob", "Charlie", "David"]
# }
#
# orders = {
#   "order_id": [101, 102, 103, 104],
#   "customer_id": [1, 2, 2, 4],
#   "amount": [250, 300, 150, 400]
# }
#
# Then:
# - merge the two DataFrames on "customer_id"
# - keep only matching rows
#
# Print the final merged DataFrame

import pandas as pd

customers = {
    "customer_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"]
}

orders = {
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 2, 4],
    "amount": [250, 300, 150, 400]
}

customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)

customers_id = pd.merge(customers_df, orders_df, on= "customer_id", how = "inner")

print("Final DataFrame:")
print(customers_id)