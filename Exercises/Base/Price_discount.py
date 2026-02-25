#Chiedi prezzo e percentuale di sconto, poi mostra il prezzo finale.

def apply_discount():
    """Returns the discounted price given the original price and a discount"""
    price = float(input("Please, insert a price: "))
    discount = float(input("Please, indicate a discount to apply to the price(between 1-100): % "))
    value_discounted = price *(discount/100)
    final_price = price - value_discounted
    return final_price

discounted_price = apply_discount()
print(f"The discounted price is {discounted_price:.2f} €.")