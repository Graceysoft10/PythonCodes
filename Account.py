class Account:
    def __init__(self):
        self.accountName = "Helen"
        self.accountNumber = "0123456"
        self.balance = 1000
        self.pin = 1234

    @staticmethod
    def get_accountName(accountName):
        return accountName

    def get_balance(self, balance):
        pass

    def get_pin(self, pin):
        pass

    def withdraw(self, pin, amount):
        if self.balance > 0:
            self.balance -= amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
