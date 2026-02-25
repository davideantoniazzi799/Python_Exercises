#Crea una funzione create_order che accetti:
# - product (obbligatorio)
# - price (default = 0)
# - *extras (es: ingredienti extra)
# - **details (es: delivery, address, note)

# La funzione deve:
# - stampare il prodotto e il prezzo
# - stampare gli extra se presenti
# - stampare i dettagli se presenti
#
# Rispetta l’ordine corretto degli argomenti.

def create_order(product, price = 0, *extras, **details):
    print(f"The {product} costs {price} €.")

    if extras:
        print(f"You can add extra options such as {extras}.")
    else:
        print("No extra options.")

    if details:
        for k, v in details.items():
            print(f"{k}: {v}")
    else:
        print("No additional details.")

create_order("sandwich",
             8,
             "Mayo", "Onions",
             Delivery = "Yes", Address = "Viale Mazzini 13", Notes = "No")