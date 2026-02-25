#Dalla lista [1, 2, 3, 4, 5] crea un dizionario
#dove le chiavi sono i numeri e i valori siano "even" se il numero è pari, "odd" se dispari.

new_dict = {number:"even" if number % 2 == 0 else "odd" for number in range(1,6)}
print(new_dict)