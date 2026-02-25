# Using the same 4×6 matrix:
# Create a new array where:
# - values < 10 become -1
# - values ≥ 10 remain unchanged
# 
# Print:
# - original array
# - modified array

import numpy as np

arr = np.arange(1,25).reshape(4,6)
arr_modify = np.where(arr >= 10, arr, -1)

print("Original array:", arr)
print("Modified array:", arr_modify)