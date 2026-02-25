# Using the same DataFrame:
# - print a statistical summary using .describe()
#
# Then:
# - print only the mean of "age"
# - print only the standard deviation of "score"

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 28, 40],
    "score": [85, 90, 88, 92, 70]
}

df = pd.DataFrame(data)

print("Statistical summary:")
print(df.describe())
print("Average mean:", round(df["age"].mean(), 2))
print("Score's standard deviation:", round(df["score"].std(), 2))