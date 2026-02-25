#Chiedi due numeri e stampa il risultato della divisione.
# Gestisci:
# - divisione per zero
# - input non numerico

try:
    first_number = int(input("Please, type the first number: "))
    second_number = int(input("Please, type the second number: "))
    result = first_number/second_number
except ValueError as value_error:
    print("Error:", value_error)
except ZeroDivisionError as ZeroDiv_Error:
    print("Error:", ZeroDiv_Error)
else:
    print("Your numbers are correct.")
    print(f"{first_number} / {second_number} = {result:.2f}")