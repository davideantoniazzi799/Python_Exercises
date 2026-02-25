#Chiedi un numero e:
# - convertilo in int
# - dividilo per 100
# Gestisci separatamente:
# - input non valido
# - divisione per zero

try:
    user_input = int(input("Please, insert a number: "))
    div_100 = user_input/100
except ValueError:
    print("Input must be a number.")
else:
    print(f"{user_input} / 100 = {div_100}")