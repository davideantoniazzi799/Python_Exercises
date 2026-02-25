#Scrivi un programma che:
# 1 - Conta quante volte appare ogni parola
# 2 - Ordina le parole dalla più frequente alla meno frequente
# 3 - Salva il risultato in top_words.txt

with open("clean_text.txt") as file_input, open("top_words.txt", mode = "w") as file_output:
    words = file_input.read().split()
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    val_based_dict = {k:v for k,v in sorted(dict_words.items(),
                                            key = lambda item:item[1], reverse = True)}


    for word, count in val_based_dict.items():
        file_output.write(f"{word}: {count}\n")