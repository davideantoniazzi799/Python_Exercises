# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#   "age": [25, None, 35, None, 40],
#   "score": [85, 90, None, 88, 70]
# }
#
# Then:
# - fill missing ages with the average age
# - fill missing scores with the median score
# - create a new column "passed":
#       True if score >= 80
#       False otherwise
# - print only the people who passed
#
# Print the final filtered DataFrame

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, None, 35, None, 40],
    "score": [85, 90, None, 88, 70]
}

df = pd.DataFrame(data)

df["age"].fillna(df["age"].mean(), inplace=True)
df["score"].fillna(df["score"].median(), inplace=True)
df["passed"] = df["score"] >= 80

print("Students who passed:")
print(df[df["passed"] == True])