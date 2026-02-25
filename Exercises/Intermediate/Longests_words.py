#Dato un testo, stampa le 3 parole più lunghe.

sentence = input("Inserisci una frase: ")
words = sentence.split()

top3 = []  # lista che conterrà le 3 parole più lunghe

for word in words:
    # aggiungi la parola se la lista ha meno di 3 parole
    if len(top3) < 3:
        top3.append(word)
    else:
        # trova la parola più corta nella lista top3
        min_word = min(top3, key=len)
        # se la parola corrente è più lunga, sostituiscila
        if len(word) > len(min_word):
            top3[top3.index(min_word)] = word

print("Le 3 parole più lunghe sono:", top3)