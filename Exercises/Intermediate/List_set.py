#Crea una lista con elementi ripetuti e ricreala senza duplicati usando un set.
def set_list(a):
    """Applies the function set to an input list. The final list has no duplicates."""
    return set(a)

list_elements = [1,2,23,34,2,1,34,56,23,1,23,7]
final_list = set_list(list_elements)
print(final_list)