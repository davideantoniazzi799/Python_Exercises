# Crea due classi:
# 1 - Vehicle (genitore)
# - Attributi: brand, speed
# - Metodo: drive() → stampa "The {brand} is driving at {speed} km/h"
# 2 - Car (figlia di Vehicle)
# - Override del metodo drive() → stampa "The {brand} car is racing at {speed} km/h"
# - Aggiungi un metodo accelerate(amount) che aumenta speed di amount
# 3 - Crea una classe Motorbike che eredita da Vehicle:
# - Override di drive() → stampa "The {brand} motorbike is zooming at {speed} km/h"

# - Crea un oggetto Motorbike e chiama drive().

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"The {self.brand} is driving at {self.speed} km/h.")

class Car(Vehicle):
    def accelerate(self, amount):
        self.speed += amount

    def drive(self):
        print(f"The {self.brand} car is racing at {self.speed} km/h.")

class Motorbike(Vehicle):
    def drive(self):
        print(f"The {self.brand} motorbike is zooming at {self.speed} km/h")

motorbike = Motorbike("Yamaha", 200)
motorbike.drive()