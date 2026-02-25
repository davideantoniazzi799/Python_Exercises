#Chiedi due numeri all’utente e stampa la loro somma.

number_1 = float(input("Please, insert a number: "))
number_2 = float(input("Please, insert a second number: "))

def somma(a,b):
    """Restituisce la somma di due numeri"""
    return a + b

result = somma(a = number_1, b = number_2)

print(f"Their sum is {result:.2f}")