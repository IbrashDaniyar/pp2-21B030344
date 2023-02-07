class Account:
    owner = " "
    balance = 0
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    
    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'
    
    def deposit(self, amount):
        self.balance += amount
        return "Deposit Accepted"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return "Withdrawl Accepted:"
        return "Funds Unavailable!"