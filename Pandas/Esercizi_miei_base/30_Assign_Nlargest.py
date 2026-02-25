# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#   "sales": [250, 400, 150, 500, 300]
# }
#
# Then:
# - create a column "bonus" where:
#     bonus = 10% of sales
#
# - create a column "total_pay":
#     total_pay = sales + bonus
#
# - select the TOP 3 employees by total_pay
#
# Print the final DataFrame

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "sales": [250, 400, 150, 500, 300]
}

df = pd.DataFrame(data)

df_2 = df.assign(
    bonus = round(0.10 * df["sales"], 2),
    total_pay = lambda x: x["sales"] + round(0.10 * x["sales"], 2)
)

print("Top 3 employees by total pay:")
print(df_2.nlargest(3, "total_pay"))