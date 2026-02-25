#Dato il dizionario {"a": 1, "b": 2, "c": 3},
# crea un nuovo dizionario con chiavi e valori invertiti.

dict_original = {"a": 1, "b": 2, "c": 3}
inverted_dict = {value:key for (key,value) in dict_original.items()}
print(inverted_dict)