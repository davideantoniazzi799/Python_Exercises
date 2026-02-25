# Create this DataFrame:
# data = {
#   "city": ["Rome", "Rome", "Milan", "Milan", "Naples", "Naples"],
#   "year": [2023, 2024, 2023, 2024, 2023, 2024],
#   "sales": [100, 120, 90, 110, 80, 95]
# }
#
# Then:
# - create a pivot table where:
#     rows = city
#     columns = year
#     values = average sales
#
# Print the pivot table

import pandas as pd

data = {
    "city": ["Rome", "Rome", "Milan", "Milan", "Naples", "Naples"],
    "year": [2023, 2024, 2023, 2024, 2023, 2024],
    "sales": [100, 120, 90, 110, 80, 95]
}

df = pd.DataFrame(data)

pv_table = pd.pivot_table(df, values="sales", index = "city", columns="year", aggfunc="mean")
print("Average score:")
print(pv_table)