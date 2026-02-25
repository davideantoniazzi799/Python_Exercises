# Create a NumPy array with these values: [2, 4, 6, 8, 10]
# Create a new array where:
# - every element is multiplied by 3
# 
# Print both arrays

import numpy as np

arr1 = np.arange(2,12,2)
arr_times_3 = arr1 * 3

print("First array:", arr1)
print("First array x 3:", arr_times_3)