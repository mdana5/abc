class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return False
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")
        print(f"Deposited: ${amount} | New Balance: ${self.balance}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance}")
            return False
        self.balance -= amount
        self.transactions.append(f"Withdrawal: -${amount}")
        print(f"Withdrawn: ${amount} | New Balance: ${self.balance}")
        return True
    
    def view_balance(self):
        print(f"Current Balance: ${self.balance}")
        return self.balance
    
    def view_history(self):
        print("\n--- Transaction History ---")
        for transaction in self.transactions:
            print(transaction)
        print(f"Final Balance: ${self.balance}\n")


def main():
    account = Account(0)
    
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. View Balance\n4. View History\n5. Exit")
        choice = input("Choose option: ").strip()
        
        if choice == "1":
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == "3":
            account.view_balance()
        elif choice == "4":
            account.view_history()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()