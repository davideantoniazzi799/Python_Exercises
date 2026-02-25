#Chiedi all’utente i km e converti in miglia.

def km_to_miles(a):
    "Converts km in miles"
    return a * 0.62137119

km = float(input("Insert a distance in km: "))
print(f"It is equal to {km_to_miles(km):.2f} miles")