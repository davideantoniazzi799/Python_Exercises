#Crea una lista dei numeri da 1 a 50 che siano multipli di 3 o di 5.

new_list = [number for number in range(1,51) if (number % 3 == 0) or (number % 5 == 0)]
print(new_list)