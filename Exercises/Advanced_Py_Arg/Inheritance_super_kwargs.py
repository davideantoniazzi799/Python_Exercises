# Crea:
# - una classe Vehicle con:
#       attributo brand
#       **kwargs per caratteristiche extra

# - una classe Car che eredita da Vehicle e aggiunge:
#       doors

# Usa super() per passare correttamente i parametri
#
# Crea un oggetto Car con caratteristiche extra (color, electric).

class Vehicle:
    def __init__(self, brand, **extra_data):
        self.brand = brand
        self.extra_data = extra_data

class Car(Vehicle):
    def __init__(self, brand, doors = 1, **extra_data):
        if doors < 1:
            raise ValueError("A car must have at least one door")

        super().__init__(brand, **extra_data)
        self.doors = doors

car = Car(brand = "Porsche", doors = 2, color = "dark grey", electric = False)