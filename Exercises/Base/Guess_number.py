#Il computer sceglie un numero casuale da 1 a 50;
#l’utente deve indovinarlo con feedback “troppo alto/basso”.
import random

right_number = random.randint(1,50)
still_guessing = False

while not still_guessing:
    user_guess = int(input("Guess the extracted number between 1 and 50: "))

    if 1 <= user_guess <= 50:
        if user_guess < right_number:
            print("Too low. Try again :(")
        elif user_guess > right_number:
            print("Too high. Try again :(")
        else:
            print("You got it!")
            still_guessing = True
    else:
        print("Number included between 1 and 50!")