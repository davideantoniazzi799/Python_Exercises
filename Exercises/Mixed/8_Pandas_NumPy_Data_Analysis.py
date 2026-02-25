# ==========================================================
# EXERCISE 3 — Pandas & NumPy Data Analysis
# ==========================================================
# Using the loaded file data:
#
# 1) Create a Pandas DataFrame with:
#    columns: name, average
# 2) Convert "average" to NumPy array
# 3) Calculate:
#    - mean
#    - median
#    - standard deviation
# 4) Create a column "performance":
#    - "LOW" if average < 70
#    - "MEDIUM" if average BETWEEN 70 and 85
#    - "HIGH" if average > 85
# 5) Show only HIGH performers

import pandas as pd
import numpy as np

def score_average(average):
    if average < 70:
        return "LOW"
    elif 70 <= average <= 85:
        return "MEDIUM"
    else:
        return "HIGH"

df = pd.read_csv("Student_average_grade.txt", 
                 sep = "|", 
                 header = None, 
                 names = ["name", "average"])

# Clean and convert
df["name"] = df["name"].str.strip()
df["average"] = df["average"].str.strip().astype(float)

# Convert to NumPy array
avg_array = df["average"].to_numpy()

print("Average grade:", round(np.mean(avg_array), 2))
print("Median grade:", np.median(avg_array))
print("Standard deviation grade:", round(np.std(avg_array), 2))

df["performance"] = df["average"].apply(score_average)

filter = df["performance"] == "HIGH"

print("Students with high performance:")
print(df[filter])