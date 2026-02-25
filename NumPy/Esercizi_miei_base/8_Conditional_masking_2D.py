# Using the same 3x4 array:
#
# Create a new array that contains only:
# - values greater than 5
# - and divisible by 2
#
# Print the result

import numpy as np

arr_2D = np.arange(1,13).reshape(3,4)

arr2D_mask = arr_2D[(arr_2D > 5) & (arr_2D % 2 == 0)]

print("Filtered array:", arr2D_mask)