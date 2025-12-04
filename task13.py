
import json
import os

FILENAME = "task13.json"

class BankAccount:
    id_counter = 0

    def __init__(self, name, phone, initial_amount=5000):
        BankAccount.id_counter += 1
        self.id = BankAccount.id_counter
        self.name = name
        self.phone = phone
        self.balance = initial_amount

    def check_balance(self):
        print(f"\n--- Account Info ---")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance} Rs\n")

    def deposit(self, amount):
        self.balance += amount
        print(f"Money Deposited Successfully\nAvailable Balance: {self.balance} Rs\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Cannot Withdraw {amount} from {self.balance} Rs\n")
        else:
            self.balance -= amount
            print(f"Money Withdrawn Successfully\nAvailable Balance: {self.balance} Rs\n")

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "phone" : self.phone,
            "balance" : self.balance
        }  
    
    
    @classmethod
    def from_dict(cls, data):
        obj = cls.__new__(cls)  
        obj.id = data["id"]
        obj.name = data["name"]
        obj.phone = data["phone"]
        obj.balance = data["balance"]
        return obj


class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.load_data( )

    
    
    def save_data(self):
        data = {
            "accounts": [acc.to_dict() for acc in self.accounts.values()],
            "id_counter": BankAccount.id_counter
        }

        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=4)
        self.load_data()

    def load_data(self):
        if not os.path.exists(FILENAME):
            return  

        with open(FILENAME, "r") as f:
            data = json.load(f)

        self.accounts = {}

        for acc_data in data["accounts"]:
            acc = BankAccount.from_dict(acc_data)
            self.accounts[acc.id] = acc

        BankAccount.id_counter = data.get("id_counter", 0)



    @staticmethod
    def print_main_menu():
        print("\n--- Xylisys Bank ---")
        print("1. Create Account")
        print("2. Login to Account")
        print("3. Exit")

    @staticmethod
    def print_account_menu():
        print("\n--- Account Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")

    def create_account(self):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        for i in self.accounts.values():
            if i.phone == phone:
                print(f"An account with phone number {phone} already exists! Try logging in.")
                return
        account = BankAccount(name, phone)
        self.accounts[account.id] = account
        print(f"\nAccount Created Successfully! Your Account ID is: {account.id}\n")

    def login(self):
        try:
            acc_id = int(input("Enter your Account ID: "))
            if acc_id in self.accounts:
                account = self.accounts[acc_id]
                print(f"\nWelcome {account.name}!")
                self.account_menu(account)
            else:
                print("Account ID not found!")
        except ValueError:
            print("Please enter a valid numeric Account ID!")

    def account_menu(self, account):
        while True:
            self.print_account_menu()
            try:
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        account.check_balance()
                    case 2:
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                        self.save_data()
                    case 3:
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                        self.save_data()
                    case 4:
                        print(f"Logging out {account.name}...\n")
                        break
                    case _:
                        print("Invalid choice. Try again.")
            except Exception as e:
                print("Invalid input:", e)

    def run(self):
        while True:
            self.print_main_menu()
            try:
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        self.create_account()
                        self.save_data()
                    case 2:
                        self.login()
                    case 3:
                        print("Thank you for banking with us!")
                        break
                    case _:
                        print("Invalid choice. Try again.")
            except Exception as e:
                print("Invalid input:", e)



bank = BankSystem()
bank.run()
