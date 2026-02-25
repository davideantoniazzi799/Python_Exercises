# Crea:
# - una classe BaseProduct con:
#       name
#       price
#       **metadata
#
# - una classe DigitalProduct che eredita da BaseProduct e aggiunge:
#       file_size
#
# Usa super() per gestire gli argomenti
# Crea un oggetto DigitalProduct con metadata extra (format, license)
# Aggiungi un metodo print_details() che stampi tutto.

class BaseProduct:
    def __init__(self, *, name, price = 0, **extra_data):

        if price < 0:
            raise ValueError("Price must be higher than 0.")

        self.name = name
        self.price = price
        self.extra_data = extra_data

    def print_details(self):
        print(f"Product name: {self.name}")
        print(f"Product price: {self.price} €")

        if self.extra_data:
            for k, v in self.extra_data.items():
                print(f"{k}: {v}")

class DigitalProduct(BaseProduct):
    def __init__(self, name, price, file_size = 0, **extra_data):
        if file_size < 0:
            raise ValueError("File size cannot be negative.")

        self.file_size = file_size

        super().__init__(name = name, price = price, **extra_data)

    def print_details(self):
        super().print_details()
        print(f"Product size: {self.file_size} MB")

dig_product = DigitalProduct(name = "Paper Research",
                             price = 43,
                             file_size = 10,
                             format = "PDF",
                             license = True)
dig_product.print_details()