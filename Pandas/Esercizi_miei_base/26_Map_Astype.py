# Create this DataFrame:
# data = {
#   "name": ["Alice", "Bob", "Charlie", "David"],
#   "score": [85, 72, 90, 60]
# }
#
# Then:
# - create a dictionary that maps:
#       A -> "Excellent"
#       B -> "Good"
#       C -> "Pass"
#       D -> "Fail"
#
# - create a column "letter_grade" where:
#       score >= 85 -> A
#       score >= 70 -> B
#       score >= 60 -> C
#       else -> D
#
# - use .map() to create a column "description"
# - convert "score" column to float
#
# Print the final DataFrame

import pandas as pd

def letter_grade(score):
    if score < 60:
        return "D"
    elif score < 70:
        return "C"
    elif score < 85:
        return "B"
    else:
        return "A"

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, 72, 90, 60]
}

grades = {
    "A": "Excellent",
    "B": "Good",
    "C": "Pass",
    "D": "Fail"
}

df = pd.DataFrame(data)

df["letter_grade"] = df["score"].apply(letter_grade)
#df["letter_grade"] = pd.cut(
#    df["score"],
#    bins=[0, 59, 69, 84, 100],
#    labels=["D", "C", "B", "A"]
#)

df["description"] = df["letter_grade"].map(grades)
df["score"] = df["score"].astype(float)

print("Final result:")
print(df)