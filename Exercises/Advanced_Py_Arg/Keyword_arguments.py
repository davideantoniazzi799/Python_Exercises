#Crea una funzione print_person che:
# 1 - accetti name, age, city
# 2 - stampi una frase formattata
# 3 - permetta di chiamare la funzione solo usando keyword arguments
#
# Prova a chiamarla con l’ordine invertito.

def print_person(*, name, age, city):
    print(f"{name} is {age} and lives in {city}.")

print_person(name = "Luca", age = 25, city = "Rome")