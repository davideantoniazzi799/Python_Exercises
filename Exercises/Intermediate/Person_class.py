#Crea una classe Persona con attributi nome e età e un metodo che stampi una descrizione.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def print_info(self):
        print(f"The user's name is {self.name} and he/she is {self.age} years old.")

    def __str__(self): #to directly print the object
        return f"{self.name} is {self.age}."


person = Person("Jake", 23)
person.print_info()
print(person)