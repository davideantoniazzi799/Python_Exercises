#Scrivi un programma che:
# 1 - Legge raw_text.txt
# 2 - Converte tutto in minuscolo
# 3 - Rimuove punteggiatura (.,!?)
# 4 - Salva il testo pulito in clean_text.txt

import string
translator = str.maketrans('', '', string.punctuation)

with open("raw_text.txt") as file_input, open("clean_text.txt", mode = "w") as file_output:
    data = file_input.read()
    lower_case = data.lower()
    clean_text = lower_case.translate(translator)
    file_output.write(clean_text)
