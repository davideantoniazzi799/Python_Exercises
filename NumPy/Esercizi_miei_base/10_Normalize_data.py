# Create a 1D NumPy array with these values:
# [100, 200, 300, 400, 500]
#
# Normalize the array using this formula:
# (x - min) / (max - min)
#
# Print:
# - original array
# - normalized array

import numpy as np

arr1D = np.array([100, 200, 300, 400, 500])

normalized_array = ((arr1D - np.min(arr1D))/(np.max(arr1D) - np.min(arr1D)))

print("Original array:", arr1D)
print("Normalized array:", normalized_array)