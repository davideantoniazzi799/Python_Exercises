#Menù che permette all’utente di eseguire più operazioni fino a quando sceglie "exit".

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

operations = {
    "sum": sum_numbers,
    "sub": sub_numbers,
    "multiply": multiply_numbers,
    "divide": div_numbers
}

while True:
    operation = input("Type either sum, sub, multiply, divide. 'Exit' to stop the calculator: ").lower()

    if operation == "exit":
        break

    if operation not in operations:
        print("Invalid operation. Please try again.")
        continue

    num_1 = float(input("Please, insert a number: "))
    num_2 = float(input("Please, insert a second number: "))

    result = operations[operation](num_1, num_2)
    if result is None:
        print("Error: cannot divide by zero!")
    else:
        print(f"The result is: {result:.2f}")