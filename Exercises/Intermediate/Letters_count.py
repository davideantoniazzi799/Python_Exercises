#Dato un testo, conta quante volte appare ogni lettera (usa un dizionario).

text = input("Type a text: ").lower()

letter_count_dict = {}

for letter in text:
    if letter in letter_count_dict:
        letter_count_dict[letter] += 1
    elif letter == " ":
        letter_count_dict["Space"] = 1
    else:
        letter_count_dict[letter] = 1

for letter in letter_count_dict:
    print(f"The letter {letter} appears {letter_count_dict[letter]} times")