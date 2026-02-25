#Crea una classe Circle con:
# - attributo: radius
# - proprietà: area → calcola 𝜋 * r²
# - proprietà: diameter → r * 2
# Niente metodi con (): devono essere property.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius * self.radius

    @property
    def diameter(self):
        return 2 * self.radius

circle = Circle(radius=3)
print(f"Area is {circle.area:.2f}")
print(f"Diameter is {circle.diameter:.2f}")