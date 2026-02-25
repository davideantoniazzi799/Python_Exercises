# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David"],
#   "age": [25, None, 35, None],
#   "score": [85, 90, None, 88]
# }
#
# Then:
# - detect missing values using .isna()
# - fill missing ages with the average age
# - fill missing scores with 0
#
# Print the final DataFrame

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, None, 35, None],
    "score": [85, 90, None, 88]
}

df = pd.DataFrame(data)

print("Missing data in the DataFrame:")
print(df.isna())

df["age"].fillna(df["age"].mean(), inplace=True)
df["score"].fillna(0, inplace=True)

# df["age"] = df["age"].fillna(df["age"].mean())
# df["score"] = df["score"].fillna(0)

print("DataFrame without missing data:")
print(df)