# Create this DataFrame:
# data = {
#   "city": ["Rome", "Rome", "Milan", "Milan", "Naples", "Naples"],
#   "year": [2023, 2024, 2023, 2024, 2023, 2024],
#   "passed": [True, False, True, True, False, True]
# }
#
# Then:
# - create a pivot table where:
#     rows = city
#     columns = year
#     values = percentage of passed students
#
# Hint:
# - True counts as 1, False as 0
# - You can use mean() to compute percentages
#
# Print the pivot table

import pandas as pd

data = {
    "city": ["Rome", "Rome", "Milan", "Milan", "Naples", "Naples"],
    "year": [2023, 2024, 2023, 2024, 2023, 2024],
    "passed": [True, False, True, True, False, True]
}

df = pd.DataFrame(data)

pv_table = pd.pivot_table(df, values="passed", index = "city", columns="year", aggfunc="mean") * 100

print("Percentage of students that passed per city and year:")
print(pv_table.round(1))