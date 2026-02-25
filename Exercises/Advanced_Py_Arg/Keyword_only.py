# Crea una classe BankAccount che:
# - abbia un attributo balance
# - abbia un metodo withdraw che:
#       accetti solo keyword arguments
#       abbia un parametro amount
#       sottragga l’importo dal saldo
#
#  Prova a chiamare withdraw:
#  - correttamente
#  - in modo errato (positional)

class BankAccount:
    def __init__(self):
        self.balance = 50

    def withdraw(self, *, amount):
        if amount <= 0:
            raise ValueError("The amount has to be greater than 0.")

        if self.balance < amount:
            raise ValueError("There is not enough money in your balance.")

        self.balance -= amount
        print("Operation completed.")
        print(f"You have {self.balance} € in your balance.")

bank_account = BankAccount()
bank_account.withdraw(amount = 10)