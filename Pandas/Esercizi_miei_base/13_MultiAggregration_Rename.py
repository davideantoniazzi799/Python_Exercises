# Create this DataFrame:
# data = {
#   "city": ["Rome", "Rome", "Milan", "Milan", "Naples", "Naples"],
#   "score": [85, 78, 90, 95, 70, 88]
# }
#
# Then:
# - group by city
# - compute:
#       - average score
#       - maximum score
#       - count of entries
# - rename columns to:
#       avg_score, max_score, total_entries
#
# Print the final DataFrame

import pandas as pd

data = {
    "city": ["Rome", "Rome", "Milan", "Milan", "Naples", "Naples"],
    "score": [85, 78, 90, 95, 70, 88]
}

df = pd.DataFrame(data)

result = (
    df
    .groupby("city")
    .agg(avg_score=("score", "mean"), max_score=("score", "max"), total_entries=("score", "count"))
)

print("Final grouped DataFrame:")
print(result)