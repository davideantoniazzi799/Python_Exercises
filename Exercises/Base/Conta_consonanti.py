#Dato un testo, conta quante consonanti contiene.

consonant_list = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def consonant_count(a):
    cons_total = 0
    for letter in a:
        if letter in consonant_list:
            cons_total +=1

    return cons_total

text = input("Type a text, please: ").lower()
number_consonant = consonant_count(text)
print(f"Your text has {number_consonant} consonants")