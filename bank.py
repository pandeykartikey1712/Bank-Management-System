import datetime
from transaction_log import log_transaction
from exceptions import InsufficientBalanceError, InvalidAmountError, InvalidInputError

class Bank:
    def __init__(self, username, account_number, balance, account_type, password):
        self.__username = username
        self.__account_number = account_number
        self.__balance = balance
        self.__account_type = account_type
        self.__password = password
        self.__transactions = []
        a.append(self.__password)
    def create_transaction_table(self):
        print(f"Transaction table created for {self.__username}")

    def verify_password(self):
        attempts = 3
        while attempts > 0:
            input_password = input("Enter your password: ")
            if input_password == self.__password:
                return True
        else:
            attempts -= 1
            print(f"Incorrect password. You have {attempts} attempts left.")
        print("Too many failed attempts. Access denied.")
        return False

    def balance_enquiry(self):
        if self.verify_password():
            print(f"{self.__username}'s account balance is {self.__balance}")

    def deposit(self, amount):
        if not self.verify_password():
            return
        if amount <= 0:
            raise InvalidAmountError
        self.__balance += amount
        log_transaction(self.__account_number, "Amount Deposit", amount)
        print(f"{self.__username}, amount {amount} successfully deposited into your {self.__account_type} account.")
        self.balance_enquiry()
    def verify_pass(self,password):
        return password in a
        

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError
        elif amount > self.__balance:
            raise InsufficientBalanceError
        else:
            self.__balance -= amount
            print(f"{self.__username}, amount {amount} successfully withdrawn from your {self.__account_type} account.")
            self.balance_enquiry()

    def fund_transfer(self, receiver, amount):
        if not self.verify_password():
            return
        if amount <= 0:
            raise InvalidAmountError
        if amount > self.__balance:
            raise InsufficientBalanceError
        self.__balance -= amount
        receiver.balance += amount
        print(f"Amount {amount} successfully transferred to account {receiver}.")
        print(f"Your new balance is {self.__balance}")
        return "Done"
a=[]