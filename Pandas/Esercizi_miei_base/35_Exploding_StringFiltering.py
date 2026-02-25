# ======================
# EXERCISE 5 — Exploding & String Filtering
# ======================
# Create this DataFrame:
# data = {
# "name": ["Alice", "Bob", "Charlie"],
# "skills": ["Python,SQL", "Excel,PowerBI", "Python,Excel,SQL"]
# }
# Then:
# - split "skills" into lists
# - explode into multiple rows
# - keep only rows where skill contains "Python"
# - convert all skills to uppercase
# Print final DataFrame

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "skills": ["Python,SQL", "Excel,PowerBI", "Python,Excel,SQL"]
}

df = pd.DataFrame(data)

df["skills"] = df["skills"].str.split(",")

df_explode = df.explode("skills")

df_final = df_explode[df_explode["skills"].str.contains("Python")]

df_final.loc[:, "skills"] = df_final["skills"].str.upper()

print(df_final)