
class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0 :
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self,amount):
        if amount <= 0 :
             raise ValueError("Amount must be positive")
        self.balance -= amount
        if self.balance < amount :
            raise ValueError("Insufficient balance")
        
class Customer:
    def __init__(self, firstname, lastname):
       self.firstname = firstname
       self.lastname = lastname

account1=BankAccount("1001", 1000000)
account2=BankAccount("1002", 500000)

def try_it(label, method, amount):
    try:
        method(amount)
        print(f"{label:20} -> OK")
    except ValueError as error:
        print(f"{label:20} -> ERROR: {error}")


account = BankAccount("1001", 1000000)
try_it("withdraw 200", account.withdraw, 200)
try_it("withdraw 99999999", account.withdraw, 99999999)
try_it("withdraw -5", account.withdraw, -5)
try_it("withdraw 0", account.withdraw, 0)
try_it("deposit 300", account.deposit, 300)
try_it("deposit 0", account.deposit, 0)
try_it("deposit -500", account.deposit, -500)
print("final balance:", account.balance)