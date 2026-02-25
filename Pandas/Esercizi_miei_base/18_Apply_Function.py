# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David"],
#   "score": [85, 72, 90, 60]
# }
#
# Then:
# - create a function that returns:
#     "Excellent" if score >= 85
#     "Pass" if score >= 70
#     "Fail" otherwise
#
# - use .apply() to create a new column "grade"
#
# Print the final DataFrame

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, 72, 90, 60]
}

df = pd.DataFrame(data)

def score_mark(score):
    if score < 70:
        return "Fail"
    elif score < 85:
        return "Pass"
    else:
        return "Excellent"
    
df["grade"] = df["score"].apply(score_mark)

print("Final result:")
print(df)