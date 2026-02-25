# ======================
# EXERCISE 3 — Time Series Trends
# ======================
# Create this DataFrame:
# data = {
# "day": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
# "sales": [100, 120, 90, 150, 200]
# }
# Then:
# - convert "day" to datetime
# - create a column "prev_day_sales" using .shift()
# - create a column "daily_change" using .diff()
#
# Print final DataFrame

import pandas as pd

data = {
    "day": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "sales": [100, 120, 90, 150, 200]
}

df = pd.DataFrame(data)

df["day"] = pd.to_datetime(df["day"])
df["prev_day_sales"] = df["sales"].shift(periods=1)
df["daily_change"] = df["sales"].diff()

print("Final result:")
print(df)