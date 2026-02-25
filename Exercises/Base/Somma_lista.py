#Dato un elenco di numeri (anche scritto a mano nel codice), calcolane la somma.

list_numbers = [1,2,3,4]

def sum_list(nums):
    """Calculates the sum of the elements in a list"""
    total_value = 0
    for num in nums:
        total_value += num

    return total_value

total_sum = sum_list(nums = list_numbers)
print(f"Final sum is {total_sum}")