
class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance < amount :
            raise ValueError("Insufficient balance")
        if amount < 0 :
            raise ValueError("Amount must be positive")
        self.balance -= amount


    
class Customer:
    def __init__(self, firstname, lastname):
       self.firstname = firstname
       self.lastname = lastname
     

account1=BankAccount("1001", 1000000)
account2=BankAccount("1002", 500000)




print(account1.balance)
account1.withdraw(0)
print(account1.balance)