#Indovina un numero da 1 a 20, ma l’utente ha solo 5 tentativi.
import random

number_guess = 0
right_number = random.randint(1,20)

while number_guess < 5:
    print(f"You have to guess the mysterious number between 1 and 20. You only have {5-number_guess} tries!")
    
    if number_guess == 4:
        print("Last chance! Be careful!")

    player_guess = int(input("What's your guess? "))

    if not 1 <= player_guess <= 20:
        print("Number out of boundary! Try again.")
    else:
        if player_guess != right_number:
            number_guess += 1
            if number_guess == 5:
                print(f"\nThe number was {right_number}.")
            else:
                print("Wrong guess. Try again!")
        else:
            print("You found the right number. Well done!")
            break