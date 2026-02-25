#Chiedi il raggio all’utente e calcola area e circonferenza.
import math

PI = math.pi

def circles_area(a):
    """Return the area of circle given the radius"""
    return PI * a**2

def circumference_calc(a):
    """Returns the circumference of a circle given the radius"""
    return PI * a*2

radius = float(input("Type the circle radius: "))
area_circle = circles_area(radius)
circumference = circumference_calc(radius)
print(f"The area is {area_circle:.2f}. The circumference is {circumference:.2f}.")