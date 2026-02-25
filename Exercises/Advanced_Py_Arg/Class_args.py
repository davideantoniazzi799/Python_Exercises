# Crea una classe ShoppingCart che:
# - abbia un attributo items (lista)
# - abbia un metodo add_items(*items) che:
#       aggiunga un numero indefinito di elementi alla lista
#
# Chiama il metodo più volte con quantità diverse di elementi.

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, *items):
        self.items.extend(items)

    def print_items(self):
        if self.items:
            print(f"Items in the cart: {self.items}")
        else:
            print("Cart empty.")

shoppingcart = ShoppingCart()
shoppingcart.add_items()#"Mayo","Pasta","Olive Oil","Ice-cream")
shoppingcart.print_items()