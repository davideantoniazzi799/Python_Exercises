# Crea una classe BankAccount con:
# - attributo: balance (parte da 0)
# - metodo deposit(amount)
# - metodo withdraw(amount)
#   - se il prelievo è impossibile → stampa errore
# - proprietà is_empty che ritorna True se il saldo è 0

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError()

        self.balance -= amount

    @property
    def is_empty(self):
        return self.balance == 0

acc = BankAccount()
acc.deposit(100)
acc.withdraw(80)
print(acc.balance)
print(acc.is_empty)