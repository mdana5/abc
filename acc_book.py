class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be positive!"
        
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")
        return True, f"Deposited ${amount}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive!"
        
        if amount > self.balance:
            return False, "Insufficient funds!"
        
        self.balance -= amount
        self.transactions.append(f"Withdrawal: -${amount}")
        return True, f"Withdrawn ${amount}"

    def view_balance(self):
        return self.balance

    def view_history(self):
        return self.transactions
