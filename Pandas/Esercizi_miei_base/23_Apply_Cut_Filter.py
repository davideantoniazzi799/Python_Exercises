# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#   "score": [45, 67, 82, 90, 73, 58]
# }
#
# Then:
# - create a column "level" using pd.cut():
#     0–59  -> "Low"
#     60–79 -> "Medium"
#     80–100 -> "High"
#
# - create a column "passed":
#     True if level is "Medium" or "High"
#     False otherwise
#
# - print only students who passed

import pandas as pd

def passed_exam(mark):
    if mark == "Low":
        return False
    else:
        return True

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "score": [45, 67, 82, 90, 73, 58]
}

df = pd.DataFrame(data)

bins = [0, 59, 79, 100]
lab = ["Low", "Medium", "High"]

df["level"] = pd.cut(df["score"], bins=bins, labels=lab, include_lowest=True)

df["passed"] = df["level"].apply(passed_exam)
#df["passed"] = df["level"].isin(["Medium", "High"])

print("Students who passed the test:")
print(df[df["passed"]])