#Chiedi una parola e verifica se è palindroma.

def check_palindrome(a):
    """Returns true if a word is palindrome."""
    lst = list(a)
    for i in range(len(lst)):
        if lst[i] != lst[-(i + 1)]:
            return False
    return True

word = input("Please, type a word: ").lower()
if check_palindrome(word):
    print(f"{word} is palindrome!")
else:
    print(f"{word} is not palindrome.")