

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Your current balance is: {self.balance}')
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print(f'Insufficient Funds')
            print(f'Your current balance is: {self.balance}')
            return self
        else:
            self.balance -= amount
            print(f'Your current balance is: {self.balance}')
            return self
        
    def user_balance(self):
        print(f'Your current balance is: {self.balance}')
        return self



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.user_balance()
        return self



Sokka = User('Sokka', 'boomerangGuy@noPowers.net')


Sokka.make_deposit(100).make_withdraw(50).display_user_balance()

#make dictionary - use key for account number?
