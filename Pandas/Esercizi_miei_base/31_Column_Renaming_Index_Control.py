"""
======================
EXERCISE 1 — Column Renaming & Index Control
======================
Create this DataFrame:
data = {
"Name": ["Alice", "Bob", "Charlie"],
"Score": [85, 90, 78],
"City": ["Rome", "Milan", "Rome"]
}
Then:
- rename columns to lowercase
- set "Name" as the index
- reset the index back to default
Print all steps
"""

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 90, 78],
    "City": ["Rome", "Milan", "Rome"]
}

df = pd.DataFrame(data)

print("\nORIGINAL DATAFRAME")
print(df)

# Rename columns
df_renamed = df.rename(columns={"Name": "name", "Score": "score", "City": "city"})
print("\nRENAMED COLUMNS")
print(df_renamed)

# Set index
df_indexed = df_renamed.set_index("name")
print("\nSET NAME AS INDEX")
print(df_indexed)

# Reset index
df_reset = df_indexed.reset_index()
print("\nRESET INDEX")
print(df_reset)