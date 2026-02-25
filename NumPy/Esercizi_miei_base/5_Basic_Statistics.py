# Create a NumPy array with these values: [5, 10, 15, 20, 25]
# Compute and print:
# - mean
# - minimum
# - maximum
# - sum

import numpy as np

arr = np.arange(5,30,5)

print("Array average:", np.round(np.mean(arr),2))
print("Array minimum:", np.min(arr))
print("Array maximum:", np.max(arr))
print("Array sum:", np.sum(arr))