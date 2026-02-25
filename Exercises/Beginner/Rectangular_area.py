#Chiedi base e altezza e calcola l’area.

def area_calculation (base, height):
    return base * height

base = float(input("Insert the rectangle's base: "))
height = float(input("Insert the rectangle's height: "))

area = area_calculation(base = base, height = height)
print(f"The total area is {area:.2f}")