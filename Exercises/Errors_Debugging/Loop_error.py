#Chiedi numeri all’utente in un ciclo infinito.
# - se inserisce exit il programma termina
# - se l’input non è valido → gestisci l’errore senza far crashare il programma
# - stampa la somma totale dei numeri inseriti

tot_sum = 0

while True:
    user_input = input("Please, insert a number or type 'Exit' to stop: ").strip().lower()

    if user_input == "exit":
        break

    try:
        str_to_int = int(user_input)
        tot_sum += str_to_int
    except ValueError:
        print("Please, provide a valid number.")
    else:
        print(f"The total sum is {tot_sum}.")