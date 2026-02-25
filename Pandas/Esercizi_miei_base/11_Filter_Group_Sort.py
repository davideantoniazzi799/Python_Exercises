# Create this DataFrame:
# data = {
#   "city": ["Rome", "Milan", "Rome", "Naples", "Milan", "Rome", "Naples"],
#   "age": [25, 30, 35, 28, 40, 22, 31],
#   "score": [85, 90, 78, 88, 95, 80, 70]
# }
#
# Then:
# - keep only rows where age >= 30
# - group by city
# - compute the average score per city
# - sort results by average score descending
#
# Print the final result

import pandas as pd

data = {
    "city": ["Rome", "Milan", "Rome", "Naples", "Milan", "Rome", "Naples"],
    "age": [25, 30, 35, 28, 40, 22, 31],
    "score": [85, 90, 78, 88, 95, 80, 70]
}

df = pd.DataFrame(data)

cities = df[df["age"] >= 30].groupby("city")["score"].mean().sort_values(ascending=False)

print("Average score by city with age older than 30:")
print(cities)