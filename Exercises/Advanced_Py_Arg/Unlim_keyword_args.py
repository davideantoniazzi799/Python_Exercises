#Crea una funzione print_profile che:
# accetti solo keyword arguments
# stampi ogni coppia chiave → valore su una riga
# funzioni con qualsiasi numero di dati
#
# Usa un nome diverso da kwargs (es: data).

def print_profile(**profile_data):
    for (key,value) in profile_data.items():
        print(f"{key}: {value}")

print_profile(name = "Luca", age = 25)