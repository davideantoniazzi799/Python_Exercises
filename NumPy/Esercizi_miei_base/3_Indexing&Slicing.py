# Create an array with numbers from 0 to 20
# Print:
# - the first 5 elements
# - the last 5 elements
# - only the even numbers

import numpy as np

arr = np.arange(0,21)
mask = arr%2 == 0
arrEven = arr[mask]

print("First 5 elements of the array:", arr[:5])
print("Last 5 elements of the array:", arr[-5:])
print("Even numbers in the array:", arrEven)