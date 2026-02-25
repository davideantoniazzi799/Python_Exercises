#Chiedi un numero e stampa se è pari o dispari.

def type_of_number(a):
    """Calculates if a number is even or uneven"""
    if (a % 2) == 0:
        print(f"{a} is an even number!")
    else:
        print(f"{a} is an odd number!")

number = int(input("Insert a number please: "))
type_of_number(a=number)