#Dato un testo, conta quante volte appare ogni parola.

text = input("Please, type a text: ")
list_words = text.split()
word_count_dict = {}

for word in list_words:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

for word, count in word_count_dict.items():
    print(f"The word '{word}' appears {count} times in your text.")