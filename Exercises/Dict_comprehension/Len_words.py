#Dalla lista ["python", "is", "fun"] crea un dizionario
#in cui le chiavi sono le parole e i valori la loro lunghezza.

words = ["python", "is", "fun"]
new_dict = {word:len(word) for word in words}
print(new_dict)