from account import BankAccount
from customer import Customer
from transaction import Transaction


def try_it(label, method, amount):
    try:
        method(amount)
        print(f"{label:20} -> OK")
    except ValueError as error:
        print(f"{label:20} -> ERROR: {error}")


customer = Customer("ali", "rezaei")
print(customer.full_name())
account = BankAccount("1001", 1000000, customer)
account_b = BankAccount("1002", 0, customer)
customer.firstname = "Reza"
print(account_b.owner.firstname)
print(account.owner is account_b.owner)
print(account.owner.full_name())
try_it("withdraw 200", account.withdraw, 200)
try_it("withdraw 99999999", account.withdraw, 99999999)
try_it("withdraw -5", account.withdraw, -5)
try_it("withdraw 0", account.withdraw, 0)
try_it("deposit 300", account.deposit, 300)
try_it("deposit 0", account.deposit, 0)
try_it("deposit -500", account.deposit, -500)
print("final balance:", account.balance)
assert account.balance == 1000100, "balance is wrong"
