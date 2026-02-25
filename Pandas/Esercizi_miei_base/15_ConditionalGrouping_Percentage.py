# Create this DataFrame:
# data = {
#   "city": ["Rome", "Milan", "Rome", "Naples", "Milan", "Rome"],
#   "score": [85, 90, 78, 88, 95, 80]
# }
#
# Then:
# - create a column "passed":
#       True if score >= 80
#       False otherwise
# - group by city
# - compute the percentage of passed students per city
#
# Print the final result as a DataFrame

import pandas as pd

data = {
    "city": ["Rome", "Milan", "Rome", "Naples", "Milan", "Rome"],
    "score": [85, 90, 78, 88, 95, 80]
}

df = pd.DataFrame(data)

df["passed"] = df["score"] >= 80

result = df.groupby("city").agg(total_students = ("city", "count"),
                                total_passed = ("passed", "sum"))

result["percentage_passed"] = round((result["total_passed"]/result["total_students"]) * 100, 2)

print(result)