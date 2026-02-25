#Chiedi un numero e calcola il quadrato.
# - usa try / except
# - usa else per stampare il risultato solo se non ci sono errori

try:
    user_input = float(input("Please, insert a number: "))
except ValueError:
    print("Input must be a number.")
else:
    print(f"{user_input} ^ 2 = {user_input**2:.2f}")