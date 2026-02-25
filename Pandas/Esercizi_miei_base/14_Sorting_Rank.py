# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#   "score": [85, 90, 85, 92, 70]
# }
#
# Then:
# - sort by score descending
# - create a new column "rank" where:
#       highest score = rank 1
#       next highest = rank 2
#       etc.
#
# Print the final DataFrame

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "score": [85, 90, 85, 92, 70]
}

df = pd.DataFrame(data)

final_df = df.sort_values("score", ascending=False)
final_df["rank"] = final_df["score"].rank(method = "dense", ascending=False)

print("Final Dataframe:")
print(final_df)