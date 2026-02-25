#Crea una classe User che:
# - accetti name come argomento obbligatorio
# - accetti dati aggiuntivi dinamici usando **kwargs
# - salvi questi dati in un attributo extra_data
# - abbia un metodo print_info() che stampi:
#       il nome
#       tutte le coppie chiave → valore di extra_data
#
# Prova a creare un utente con email, city, age.

class User:
    def __init__(self, *, name, **extra_data):
        self.name = name
        self.extra_data = extra_data

    def print_info(self):
        print(self.name)

        if self.extra_data:
            for k, v in self.extra_data.items():
                print(f"{k}: {v}")
        else:
            print("No additional details.")

user = User(name = "Luca", email = "luca.rossi@gmail.com", city = "Rome", age = 25)
user.print_info()