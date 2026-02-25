# Using the same DataFrame:
# - sort by "score" descending
# - sort by "age" ascending
#
# Print both results

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 28, 40],
    "score": [85, 90, 88, 92, 70]
}

df = pd.DataFrame(data)

print("Dataframe sorted from highest to lowest score:")
print(df.sort_values("score", ascending=False))

print("Dataframe sorted from youngest to oldest:")
print(df.sort_values("age"))