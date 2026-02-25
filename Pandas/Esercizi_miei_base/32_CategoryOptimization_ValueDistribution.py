# ======================
# EXERCISE 2 — Category Optimization & Value Distribution
# ======================
# Create this DataFrame:
# data = {
# "product": ["Apple", "Banana", "Apple", "Orange", "Banana", "Apple"],
# "price": [1.2, 0.8, 1.1, 1.5, 0.9, 1.3]
# }
# Then:
# - convert "product" to categorical type
# - count how often each product appears (percentage form)
# - replace:
#       "Apple" → "APPLE"
#       "Banana" → "BANANA"
# Print final DataFrame and distribution


import pandas as pd

data = {
    "product": ["Apple", "Banana", "Apple", "Orange", "Banana", "Apple"],
    "price": [1.2, 0.8, 1.1, 1.5, 0.9, 1.3]
}

df = pd.DataFrame(data)

df_category = df.astype({"product":"category"})
df_category["product"] = df_category["product"].replace({
    "Apple": "APPLE",
    "Banana": "BANANA"
})
df_value_counts = round(df_category["product"].value_counts(normalize=True) * 100, 2)

print("Final DataFrame:")
print(df_value_counts)