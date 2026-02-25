# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#   "score": [85, None, 92, 88, None]
# }
#
# Then:
# - fill missing scores with the mean score
# - sort by score descending
# - create a column "rank" where:
#     highest score = 1
#     next = 2
#     etc.
#
# Print the final DataFrame

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "score": [85, None, 92, 88, None]
}

df = pd.DataFrame(data)

df["score"].fillna(round(df["score"].mean(), 2), inplace=True)
df_sorted = df.sort_values("score", ascending=False)
df_sorted["rank"] = df_sorted["score"].rank(method = "dense", ascending=False).astype(int)

print("Final result:")
print(df_sorted)