#Chiedi una frase e conta quante vocali contiene.

vocals = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def count_vocals(a):
    """Takes a sentence and returns the number of vocals in it"""
    list_letters = list(a)
    vocals_count = 0
    for i in range(0, len(list_letters)):
        if list_letters[i] in vocals:
            vocals_count += 1

    return vocals_count

sentence = input("Please, insert a sentence: ")
tot_vocals = count_vocals(a = sentence)
print(f"There are {tot_vocals} in your sentence")