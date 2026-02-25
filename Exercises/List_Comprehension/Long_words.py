#Dalla lista ["ciao", "python", "list", "comprehension", "ok"]
#crea una lista contenente solo le parole con più di 4 lettere.

words = ["ciao", "python", "list", "comprehension", "ok"]
new_list = [word for word in words if len(word)>4]
print(new_list)