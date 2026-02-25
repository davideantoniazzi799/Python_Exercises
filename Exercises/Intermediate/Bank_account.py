#Crea una classe con:
# - saldo
# - metodi: deposita(), preleva(), mostra_saldo()
#Gestisci il caso in cui il prelievo supera il saldo.

class Balance:
    def __init__(self):
        self.money = 0

    def deposit(self, money):
        self.money += money

    def withdraw(self, amount):
        if self.money < amount:
            print(f"Withdraw not possible. There are {self.money} € in your bank account.")
        else:
            self.money -= amount

    def show_total(self):
        print(f"There are {self.money} € in your bank account.")

options = ["total", "deposit", "withdraw", "exit"]

balance = Balance()

request = input("Welcome! Please, select either 'Total', 'Deposit', 'Withdraw' or 'Exit': ").lower()
if request not in options:
    print("Wrong input.")

