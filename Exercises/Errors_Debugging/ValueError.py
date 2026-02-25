#Chiedi all’utente di inserire un numero intero.
#Se l’utente inserisce qualcosa che non è un numero:
# - intercetta l’errore
# - stampa un messaggio chiaro

try:
    user_input = int(input("Please, type a number: "))
except ValueError:
    print("The input must be a number.")
else:
    print(f"You typed the number {user_input}")