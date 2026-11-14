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