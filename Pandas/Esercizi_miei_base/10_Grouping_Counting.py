# Create this DataFrame:
# data = {
#   "city": ["Rome", "Milan", "Rome", "Naples", "Milan", "Rome"],
#   "score": [85, 90, 78, 88, 95, 80]
# }
#
# Then:
# - count how many entries per city
# - compute the average score per city using groupby
#
# Print both results

import pandas as pd

data = {
    "city": ["Rome", "Milan", "Rome", "Naples", "Milan", "Rome"],
    "score": [85, 90, 78, 88, 95, 80]
}

df = pd.DataFrame(data)
cities = df.groupby("city").mean()
# cities = df.groupby("city")["score"].mean()

print("Entries for column:", df["city"].value_counts())

print("Average score per city:")
print(cities)