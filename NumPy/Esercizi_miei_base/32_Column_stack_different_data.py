# Create:
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 88]
# 
# Use NumPy to:
# - combine them into a 2D array where each row is (name, score)
# 
# Print the result and its dtype.

import numpy as np

names = np.array(["Alice", "Bob", "Charlie"])
scores = np.array([85, 90, 88])

arr_combined = np.column_stack((names, scores))

#arr_combined = np.array(
#    list(zip(names, scores)),
#    dtype=[("name", "U10"), ("score", "i4")]
#)

print("Names and scores:", arr_combined)
print("Data type:", arr_combined.dtype)