#Crea una classe Rectangle che abbia:
# - due attributi: width e height
# - un metodo chiamato area() che ritorna area = base * altezza
# - un metodo chiamato perimeter() che ritorna il perimetro

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return self.height * 2 + self.width * 2

rect = Rectangle(width = 10, height = 5)

print(f"Area is {rect.area:.2f}.")
print(f"Perimeter is {rect.perimeter:.2f}")