# Crea tre classi:
# 1 - Animal (classe genitore)
#   - Attributo: name
#   - Metodo: speak() → stampa "I make a sound"
# 2 - Dog (classe figlia)
#   - Ereditata da Animal
#   - Aggiungi un metodo bark() → stampa "Woof!"
# 3 -Crea una classe Cat che erediti da Animal:
# - Metodo: meow() → stampa "Meow!"
# - Crea un oggetto Cat, chiama sia speak() che meow().

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I make a sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

cat = Cat("Cleo")
print(f"Hi! I am {cat.name}, the Cat.")
cat.speak()
cat.meow()