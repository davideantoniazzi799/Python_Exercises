#Scrivi un programma che converta una temperatura inserita dall’utente.

def celsius_to_fahrenheit(temp):
    """Returns the equivalent Fahrenheit value for a temperature in Celsius degree"""
    return (temp * 9/5) + 32

temp_celsius= float(input("Please, insert a temperature in Celsius degree: "))
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)

print(f"Your temperature is equivalent to {temp_fahrenheit:.2f} °F")