# Using the same 3x4 array:
#
# Create a copy of the array where:
# - all values < 5 are replaced with 0
# - all values >= 5 remain unchanged
#
# Print both arrays

import numpy as np

arr_2D = np.arange(1,13).reshape(3,4)

mask = arr_2D >= 5

arr2D_copy_1 = np.where(arr_2D >= 5, arr_2D, 0)

print("Original array:", arr_2D)
print("Filtered array:", arr2D_copy_1)