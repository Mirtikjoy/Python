class Bank:
    def __init__(self,account_Number,balance):
        self.account_Number = account_Number
        self.__balance = balance

# we define private as 2 dash __ 
    def __show_balance(self):
        print(f"Balance: {self.__balance}")


    def show_account(self):
        print(f"Account Number: {self.account_Number}")
        self.__show_balance()


account_Numbers = int(input("please anter yur account number: "))

account = Bank(account_Numbers,20000)
account.show_account()