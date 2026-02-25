#Crea una calcolatrice con funzioni somma, sottrai, moltiplica, dividi.

def sum_numbers(a, b):
    return a + b

def sub_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def div_numbers(a, b):
    if b == 0:
        return None  # divisione non valida
    return a / b

num_1 = float(input("Please, insert a number: "))
num_2 = float(input("Please, insert a second number: "))
operation = input("Type either sum, sub, multiply, divide: ").lower()

operations = {
    "sum": sum_numbers,
    "sub": sub_numbers,
    "multiply": multiply_numbers,
    "divide": div_numbers
}

if operation in operations:
    result = operations[operation](num_1, num_2)
    if result is None:
        print("Error: cannot divide by zero!")
    else:
        print(f"The result is: {result}")
else:
    print("Invalid operation. Please choose sum, sub, multiply, or divide.")