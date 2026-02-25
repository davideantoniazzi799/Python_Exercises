# Create this DataFrame:
# data = {
#   "order_id": [101, 102, 103, 103, 104, 105, 105],
#   "city": ["Rome", "Milan", "Rome", "Rome", "Naples", "Milan", "Milan"],
#   "amount": [100, 200, 150, 150, 300, 250, 250]
# }
#
# Then:
# - create a column "is_duplicate" using .duplicated() on "order_id"
# - create a new DataFrame with duplicates removed
# - compute total sales per city from the cleaned DataFrame
#
# Print:
# - original DataFrame
# - cleaned DataFrame
# - total sales per city

import pandas as pd

data = {
    "order_id": [101, 102, 103, 103, 104, 105, 105],
    "city": ["Rome", "Milan", "Rome", "Rome", "Naples", "Milan", "Milan"],
    "amount": [100, 200, 150, 150, 300, 250, 250]
}

df = pd.DataFrame(data)

df["is_duplicate"] = df["order_id"].duplicated()

df_noduplicates = df.drop_duplicates(subset="order_id")

total_sales_city = df_noduplicates.groupby("city")["amount"].sum()

print("Original data:")
print(df)

print("Data without duplicates:")
print(df_noduplicates)

print("Total sales per city:")
print(total_sales_city)