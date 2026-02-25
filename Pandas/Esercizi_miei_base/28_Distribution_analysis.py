# Create this DataFrame:
# data = {
#   "city": ["Rome", "Milan", "Rome", "Naples", "Milan", "Rome", "Naples", "Rome"]
# }
#
# Then:
# - compute:
#     - count of each city
#     - percentage of each city
#
# - create a DataFrame with columns:
#     "count"
#     "percentage"
#
# Print the final DataFrame

import pandas as pd

data = {
    "city": ["Rome", "Milan", "Rome", "Naples", "Milan", "Rome", "Naples", "Rome"]
}

df = pd.DataFrame(data)

count_city = df["city"].value_counts()
percentage_city = df["city"].value_counts(normalize=True)*100

result_df = pd.DataFrame({
    "count": count_city,
    "percentage": percentage_city
})

print("Final data:")
print(result_df)