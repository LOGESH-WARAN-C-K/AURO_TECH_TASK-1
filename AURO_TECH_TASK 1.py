import datetime

class Account:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('Deposit', amount, datetime.datetime.now()))
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(('Withdraw', amount, datetime.datetime.now()))
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            self.transactions.append(('Transfer to', recipient_account.user_id, amount, datetime.datetime.now()))
            recipient_account.transactions.append(('Transfer from', self.user_id, amount, datetime.datetime.now()))
            print(f"Transferred {amount} to {recipient_account.user_id}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, user_id, pin):
        if user_id in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[user_id] = Account(user_id, pin)
            print(f"Account created for user {user_id}.")

    def get_account(self, user_id):
        return self.accounts.get(user_id)

class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_account = None

    def login(self, user_id, pin):
        account = self.bank.get_account(user_id)
        if account and account.pin == pin:
            self.current_account = account
            print("Login successful.")
        else:
            print("Invalid user ID or PIN.")

    def logout(self):
        self.current_account = None
        print("Logged out.")

    def deposit(self, amount):
        if self.current_account:
            self.current_account.deposit(amount)
        else:
            print("Please log in first.")

    def withdraw(self, amount):
        if self.current_account:
            self.current_account.withdraw(amount)
        else:
            print("Please log in first.")

    def transfer(self, amount, recipient_user_id):
        if self.current_account:
            recipient_account = self.bank.get_account(recipient_user_id)
            if recipient_account:
                self.current_account.transfer(amount, recipient_account)
            else:
                print("Recipient account not found.")
        else:
            print("Please log in first.")

    def show_balance(self):
        if self.current_account:
            print(f"Current balance: {self.current_account.get_balance()}")
        else:
            print("Please log in first.")

    def show_transactions(self):
        if self.current_account:
            transactions = self.current_account.get_transactions()
            if transactions:
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions found.")
        else:
            print("Please log in first.")

class UserInterface:
    def __init__(self, atm):
        self.atm = atm

    def display_menu(self):
        print("\n1. Create account")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Show balance")
        print("7. Show transactions")
        print("8. Quit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter choice: ")

            if choice == '1':
                user_id = input("Enter user ID: ")
                pin = input("Enter PIN: ")
                self.atm.bank.create_account(user_id, pin)

            elif choice == '2':
                user_id = input("Enter user ID: ")
                pin = input("Enter PIN: ")
                self.atm.login(user_id, pin)

            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                self.atm.deposit(amount)

            elif choice == '4':
                amount = float(input("Enter amount to withdraw: "))
                self.atm.withdraw(amount)

            elif choice == '5':
                amount = float(input("Enter amount to transfer: "))
                recipient_user_id = input("Enter recipient user ID: ")
                self.atm.transfer(amount, recipient_user_id)

            elif choice == '6':
                self.atm.show_balance()

            elif choice == '7':
                self.atm.show_transactions()

            elif choice == '8':
                self.atm.logout()
                print("Thank you for using the ATM.")
                break

            else:
                print("Invalid choice. Please try again.")

# Main program
if __name__ == "__main__":
    bank = Bank()
    atm = ATM(bank)
    ui = UserInterface(atm)
    ui.run()
