# Create a NumPy array representing temperatures in Celsius:
# [0, 10, 20, 30, 40]
# Convert all values to Fahrenheit using the formula:
# F = C * 9/5 + 32
# Then:
# - compute the mean Fahrenheit temperature
# - round the result to 2 decimals

# Print:
# - original Celsius array
# - Fahrenheit array
# - mean Fahrenheit value

import numpy as np

arrCelsius = np.array([0, 10, 20, 30, 40])
arrFahr = arrCelsius * 9/5 + 32

mean_Fahr_temp = np.round(np.mean(arrFahr), 2)

print("Celsius temperatures:", arrCelsius)
print("Fahrenheit temperatures:", arrFahr)
print("Average Fahrenheit temperature:", mean_Fahr_temp)