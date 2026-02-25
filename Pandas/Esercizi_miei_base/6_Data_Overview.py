# Create a DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#   "age": [25, 30, 35, 28, 40],
#   "score": [85, 90, 88, 92, 70]
# }
#
# Then:
# - print the first 3 rows using .head()
# - print the last 2 rows using .tail()
# - print dataset info using .info()

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 28, 40],
    "score": [85, 90, 88, 92, 70]
}

df = pd.DataFrame(data)

print("First three rows:")
print(df.head(3))

print("Last two rows:")
print(df.tail(2))

print("DataFrame infomation:")
df.info()