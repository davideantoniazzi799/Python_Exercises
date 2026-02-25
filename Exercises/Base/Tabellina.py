#Chiedi un numero e stampa la sua tabellina da 1 a 10.

wrong_number = True

while wrong_number:
    number = int(input("Please, insert a number from 1 to 10: "))
    if number<1 or number >10:
        print("Error. It must be a number between 1 and 10. Type again.")
    else:
        number_table = [number*i for i in range(1,11)]
        print(f"The {number} table is {number_table}")
        wrong_number = False