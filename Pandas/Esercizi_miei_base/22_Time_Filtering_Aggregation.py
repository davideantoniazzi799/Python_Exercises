# Create this DataFrame:
# data = {
#   "order_id": [1, 2, 3, 4, 5, 6],
#   "date": ["2024-01-10", "2024-02-15", "2024-02-20", 
#            "2024-03-05", "2024-03-18", "2024-01-25"],
#   "amount": [100, 200, 150, 300, 250, 180]
# }
#
# Then:
# - convert "date" to datetime
# - keep only orders from February and March 2024
# - compute:
#     - total sales
#     - average sale amount
#
# Print both results

import pandas as pd

data = {
    "order_id": [1, 2, 3, 4, 5, 6],
    "date": ["2024-01-10", "2024-02-15", "2024-02-20", "2024-03-05", "2024-03-18", "2024-01-25"],
    "amount": [100, 200, 150, 300, 250, 180]
}

df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"])

df_Feb_March = df[(df["date"].dt.year == 2024) & 
                  ((df["date"].dt.month == 2) | (df["date"].dt.month == 3))]

#mask = df["date"].between("2024-02-01", "2024-03-31")
#df_Feb_March = df[mask]

print("Total sales in February and March:", df_Feb_March["amount"].sum())
print("Average sale amount for February and March:", round(df_Feb_March["amount"].mean(), 2))