#Dalla lista ["apple", "banana", "cherry"] crea una lista con tutte le stringhe in maiuscolo.

fruit_list = ["apple", "banana", "cherry"]
new_list = [word.upper() for word in fruit_list]
print(new_list)