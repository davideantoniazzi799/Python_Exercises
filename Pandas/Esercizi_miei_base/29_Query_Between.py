# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#   "age": [22, 35, 28, 42, 31],
#   "score": [85, 70, 90, 60, 88]
# }
#
# Then:
# - use .query() to keep only:
#     age between 25 and 40
#     AND score >= 80
#
# - sort by score descending
#
# Print the final DataFrame

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [22, 35, 28, 42, 31],
    "score": [85, 70, 90, 60, 88]
}

df = pd.DataFrame(data)

final_df = df.query("age.between(25,40,inclusive='both') & score >= 80")

print("Final result:")
print(final_df.sort_values("score", ascending=False))