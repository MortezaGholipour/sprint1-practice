from account import BankAccount
from customer import Customer


def try_it(label, method, amount):
    try:
        method(amount)
        print(f"{label:20} -> OK")
    except ValueError as error:
        print(f"{label:20} -> ERROR: {error}")


customer = Customer("ali", "rezaei")
account = BankAccount("1001", 1000000, customer)
print(account.owner.full_name(), account.balance)
