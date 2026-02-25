#Scrivi un programma che:
# 1 - Legge data.txt
# 2 - Conta quante volte appare ogni parola
# 3 - Salva il risultato in un file chiamato word_count.txt

with open("data.txt") as file_input, open("word_count.txt", mode = "w") as file_output:
    data = file_input.read()
    words = data.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    # Scrittura riga per riga
    for word, count in word_dict.items():
        file_output.write(f"{word}: {count}\n")