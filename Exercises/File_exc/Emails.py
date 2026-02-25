#Scrivi un programma che:
# 1 - Legge emails.txt
# 2 - Salva solo le email @gmail.com in gmail.txt
# 3 - Salva tutte le altre in others.txt

with open("emails.txt") as file_input, \
        open("gmail.txt", mode = "w") as file_gmail, \
        open("other.txt", mode = "w") as file_others:

    for line in file_input:
        if '@gmail.com' in line:
            file_gmail.write(line)
        else:
            file_others.write(line)