#Scrivi un programma che:
# 1 - Legge notes.txt
# 2 - Trasforma tutte le lettere in maiuscolo
# 3 - Salva il risultato in un nuovo file chiamato notes_upper.txt

with open("notes.txt") as file_input:
    data = file_input.read()
    uppercase = data.upper()
    with open("notes_upper.txt", mode = "w") as file_output:
        file_output.write(uppercase)

"""
with open("notes.txt") as file_input, open("notes_upper.txt", "w") as file_output:
    file_output.write(file_input.read().upper())
"""