#Crea una funzione calculate_average che:
# 1- accetti un numero indefinito di numeri
# 2- ritorni la media
# 3- se non viene passato nessun numero, ritorni None
#
# Usa *args.

def calculate_average(*args):
    if not args:
        return None

    return sum(args)/len(args)

average = calculate_average()
print(average)