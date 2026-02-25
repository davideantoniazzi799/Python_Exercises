#Es: 123 → "uno due tre".(Usa un dizionario per mappare le cifre).

number_dict ={
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

number_string = ""
user_number = input("Please, type numbers: ")
for number in user_number:
    if number in number_dict:
        number_string += number_dict[number] + " "

print(number_string)