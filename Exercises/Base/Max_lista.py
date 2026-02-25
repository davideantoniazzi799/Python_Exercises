#Trova il numero più grande in una lista di numeri.

numbers = [2, 5, 7, 9]

def find_max_list(a):
    """Returns the highest number in a list"""
    max_number = a[0]
    for i in range(0, len(a)):
        if a[i] >= max_number:
            max_number = a[i]

    return max_number

max_number_list = find_max_list(a = numbers)
print(f"The highest number in the list is {max_number_list}")