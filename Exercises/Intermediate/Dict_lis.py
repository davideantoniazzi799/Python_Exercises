#Hai una lista di prodotti (nome, prezzo, categoria).
#Permetti all’utente di cercare un prodotto per nome e stampane i dettagli.

products_dict = {
    "white bread":{
        "Price €": 0.50,
        "Category": "Bakery",
    },
    "chewing gum":{
        "Price €": 0.75,
        "Category": "Candies",
    },
    "broom":{
        "Price €": 1.25,
        "Category": "Cleanings",
    },
    "apple":{
        "Price €": 0.85,
        "Category": "Fruit",
    },
}

request = input("Welcome! What would you like to buy? ").lower()


if request not in products_dict:
    print(f"We are sorry, but we do not dispose of {request} in our store.")
else:
    print(f"You can find {request} at the {products_dict[request]['Category']} section. "
          f"It costs {products_dict[request]['Price €']} €.")