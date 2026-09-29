class Account:
    def __init__(self,account_Number,balance):
        self.account_Number = account_Number
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount
        print(f"rs {amount} was debited from your bank account\nThe total balance is {self.account_balance()}")

    def credit(self,amount):
        self.balance += amount
        print(f"rs {amount} is credited to your bank account\nThe total balance is {self.account_balance()}")



    def account_balance(self):
        return self.balance


account1 = Account(25060110128695,25000)
account1.debit(10000)
account1.credit(150000)