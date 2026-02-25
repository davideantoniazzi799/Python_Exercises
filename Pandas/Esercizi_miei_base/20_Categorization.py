# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#   "score": [45, 67, 82, 90, 73]
# }
#
# Then:
# - create a new column "level":
#     0–59  -> "Low"
#     60–79 -> "Medium"
#     80–100 -> "High"
#
# Hint: use pd.cut()
#
# Print the final DataFrame

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "score": [45, 67, 82, 90, 73]
}

df = pd.DataFrame(data)

bins = [0, 59, 79, 100]
lab = ["Low", "Medium", "High"]

df["level"] = pd.cut(df["score"], bins = bins, labels= lab, include_lowest=True)

print("Final result:")
print(df)