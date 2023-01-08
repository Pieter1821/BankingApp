import datetime

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
                print("insufficient funds")


def __str__(self):
    return f"Account name: {self.name}\nBalance: {self.balance}"


class TransactionLog:
    def __init__(self, name):
        self.name = name
        self.transaction = []

    def add_transaction(self, date, amount):
        self.transaction.append((date, amount))

    def write_to_file(self):
        with open(f" {self.name} _transaction.txt", 'w') as f:
            for transaction in self.transaction:
                f.write(
                    f"{transaction[0]}: {transaction[1]}\n")

    def __str__(self):
        return "\n".join([f"{transaction[0]} : {transaction[1]}"for transaction in self.transaction])


account = BankAccount("John Smith", 0)
transaction_log = TransactionLog("John Smith")

while True:
    print("Enter 1 to make a deposit, 2 to make a withdraw, 3 to print account info, 4 to print transaction log, or 5 to exit")
    choice = int(input())

    if choice == 1:
        amount = int(input("enter amount to make a deposit:  "))
        account.deposit(amount)
        
        transaction_log.add_transaction(datetime.datetime.now(), amount)
        print(account)
        print("deposit successful")

    elif choice == 2:
            amount = int(input("enter amount to make a withdraw: "))
            account.withdraw(amount)
            print("withdrawal successful")

            transaction_log.add_transaction(datetime.datetime.now(), amount)
    elif choice == 3:
        print(account)
    elif choice == 4:
         print(transaction_log.__str__())
    elif choice == 5:
        transaction_log.write_to_file()

    continue
else:
    print("invalid input")
