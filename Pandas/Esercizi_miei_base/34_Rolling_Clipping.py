# ======================
# EXERCISE 4 — Rolling Statistics & Clipping
# ======================
# Create this DataFrame:
# data = {
# "score": [45, 67, 89, 100, 34, 78, 90]
# }
# Then:
# - create a column "rolling_avg" with rolling mean of window size 3
# - clip scores so they stay between 50 and 95
# Print final DataFrame

import pandas as pd

data = {
    "score": [45, 67, 89, 100, 34, 78, 90]
}

df = pd.DataFrame(data)
df["rolling_avg"] = df["score"].rolling(window=3).mean()
df["score"] = df["score"].clip(lower=50, upper=95)

print("Final result:")
print(df)