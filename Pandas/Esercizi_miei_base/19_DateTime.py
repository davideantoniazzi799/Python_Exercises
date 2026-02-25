# Create this DataFrame:
# data = {
#   "order_id": [1, 2, 3, 4, 5],
#   "date": ["2024-01-10", "2024-02-15", "2024-03-20", "2024-01-25", "2024-03-05"],
#   "amount": [100, 200, 150, 300, 250]
# }
#
# Then:
# - convert "date" to datetime format
# - keep only rows from February 2024
#
# Print the filtered DataFrame

import pandas as pd

data = {
    "order_id": [1, 2, 3, 4, 5],
    "date": ["2024-01-10", "2024-02-15", "2024-03-20", "2024-01-25", "2024-03-05"],
    "amount": [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"])

df_february = df[(df["date"] >= "2024-02-01") & (df["date"] < "2024-03-01")]
#df_february = df[(df["date"].dt.year == 2024) & (df["date"].dt.month == 2)]

print("Final result:")
print(df_february)