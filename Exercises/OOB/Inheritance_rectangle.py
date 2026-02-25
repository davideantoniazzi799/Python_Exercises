#Crea una classe Rectangle:
# - Attributi: width, height
# - Property area → calcola width * height

# Crea una classe Square che eredita da Rectangle:
# - Override del __init__ per accettare un solo lato side
# - Deve comunque avere la property area ereditata

# -Crea un oggetto Square e stampa la sua area.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

square = Square(10)
print(f"The area is {square.area} m^2")