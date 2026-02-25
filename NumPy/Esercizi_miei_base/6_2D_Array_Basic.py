# Create a NumPy array with numbers from 1 to 12
# Reshape it into a 3x4 matrix
#
# Print:
# - the array
# - its shape
# - number of dimensions

import numpy as np

arr = np.arange(1,13)
arr_2D = arr.reshape(3,4)

print("Reshaped array:", arr_2D)
print("Array shape:", arr_2D.shape)
print("Number of dimensions:", arr_2D.ndim)