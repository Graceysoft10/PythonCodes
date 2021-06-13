import sys


class Account:

    def __init__(self, name, account_Number, Pin, amount, balance):
        self.name = name
        self.account_Number = account_Number
        self.pin = Pin
        self.amount = amount
        self.balance = balance
        self.beneficiary_acc_number = "123456789"

    def check_balance(self):
        return self.balance

    def create_pin(self):
        Pin = int(input("Create pin: "))
        self.pin = Pin
        print("Pin successfully created!")

    def deposit_cash(self, confirm_Pin, Amount_to_deposit):
        if confirm_Pin == self.pin:
            if Amount_to_deposit > 0:
                self.balance += Amount_to_deposit
            else:
                print("You can not deposit zero or negative value!")
        else:
            print("Wrong pin!")

    def withdraw_cash(self, confirm_Pin, amount_to_withdraw):
        if confirm_Pin == self.pin:
            if self.balance >= amount_to_withdraw:
                self.balance -= amount_to_withdraw
            else:
                print("Insufficient funds ")
        else:
            print("Wrong pin")

    def change_pin(self, existing_pin, new_pin):
        if existing_pin == self.pin:
            self.pin = new_pin
            print("Pin successfully changed!")
        else:
            print("Provide the existing pin please!")

    def transfer_cash(self, confirm_Pin, amount_to_send, beneficiary_acc_num):
        if confirm_Pin == self.pin:
            if beneficiary_acc_num == self.beneficiary_acc_number:
                if 0 < amount_to_send <= self.balance:
                    self.balance -= amount_to_send
                elif amount_to_send < 0:
                    print("you cannot transfer negative value")
                else:
                    print("Insufficient funds!")
            else:
                print("Wrong beneficiary account number")
        else:
            print("Wrong pin... check and try again!")


if __name__ == '__main__':
    Account = Account("Grace", 123456789, 4391, 0.00, 0.00)

print("Welcome to Royal Bank!...")
message = """To Create Pin -> press 1
To Deposit -> press 2
To Withdraw -> press 3
To Transfer -> press 4
To Check Balance -> press 5
To Change pin -> press 6
To Exist -> press 7
    """
user_input = int(input(message))
if user_input == 1:
    Account.create_pin()

    do_something_message = "Do you want to do something else?: "
    do_something = input(do_something_message)
    if do_something == "yes":
        user_input = int(input(message))

        if user_input == 2:
            confirm_pin = int(input("Confirm your pin: "))
            amount_to_deposit = int(input("Enter amount to deposit: "))
            Account.deposit_cash(confirm_pin, amount_to_deposit)
            print(f"Your account has been credited with {amount_to_deposit}")
            print(f"your balance is: {Account.check_balance()}")

            do_something = input(do_something_message)
            if do_something == "yes":
                user_input = int(input(message))

                if user_input == 3:
                    confirm_pin = int(input("Confirm your pin: "))
                    amount_to_Withdraw = int(input("Enter amount to withdraw: "))
                    Account.withdraw_cash(confirm_pin, amount_to_Withdraw)
                    print(f"You have been debited with: {amount_to_Withdraw}")
                    print(f"your balance is: {Account.check_balance()}")

                    do_something = input(do_something_message)
                    if do_something == "yes":
                        user_input = int(input(message))

                        if user_input == 4:
                            confirm_pin = int(input("Enter your pin: "))
                            amountToSend = int(input("Enter the amount you want to send: "))
                            beneficiary_acc_no = input("Enter beneficiary account number: ")
                            Account.transfer_cash(confirm_pin, amountToSend, beneficiary_acc_no)
                            print(f"You transferred {amountToSend} to {beneficiary_acc_no}")
                            print(f"your balance is: {Account.check_balance()}")

                            do_something = input(do_something_message)
                            if do_something == "yes":
                                user_input = int(input(message))

                                if user_input == 5:
                                    print(f"your balance is: {Account.check_balance()}")
                                    do_something = input(do_something_message)

                                    if do_something == "yes":
                                        user_input = int(input(message))

                                        if user_input == 6:
                                            old_pin = int(input("Enter existing pin: "))
                                            new_pin = int(input("Enter new pin: "))
                                            Account.change_pin(old_pin, new_pin)

                                            if do_something == "yes":

                                                while user_input != 0:
                                                    user_input = int(input(message))


    elif do_something == "no":
        print("Thanks for banking with us!")
        sys.exit(0)
    else:
        print("Invalid!")
        sys.exit(0)


elif user_input == 7:
    sys.exit(0)

Account.__str__()
