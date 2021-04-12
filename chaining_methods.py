#Understand how to chain methods

class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


monty = User('monty')
monty.make_deposit(100).make_deposit(300).make_deposit(50).make_withdrawal(150).display_user_balance()

python = User('python')
python.make_deposit(3000).make_deposit(420).make_withdrawal(1650).make_withdrawal(725).display_user_balance()

guido = User('guido')
guido.make_deposit(500).make_withdrawal(30).make_withdrawal(130).make_withdrawal(5).display_user_balance()

monty.transfer_money(guido, 100).display_user_balance()

guido.display_user_balance()
