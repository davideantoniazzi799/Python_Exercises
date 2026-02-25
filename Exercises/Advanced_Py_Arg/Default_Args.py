#Crea una funzione greet che:
# 1 - accetti name
# 2 - abbia un parametro language con valore di default "en"
# 3- stampi:
#   "Hello <name>" se "en"
#   "Ciao <name>" se "it"
#
#   Provala con e senza passare language.

def greet(name, language = "en"):
    if language == "it":
        print(f"Ciao {name}")
    elif language == "en":
        print(f"Hello {name}")
    else:
        print(f"Hello {name} (language '{language}' not supported)")

greet("Luca")
greet(name = "Luca", language = "it")