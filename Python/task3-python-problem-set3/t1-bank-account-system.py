class Bank_Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn: {amount}"
        else:
            return "Insufficient Balance!!"

    def display_balance(self):
        return f"Current Balance: {self.balance}"

class Savings_Account(Bank_Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)  #400*(4/100)=16
        self.balance += interest
        return f"Interest Applied: {interest}"

user1 = Savings_Account("5F00H08K", "Deepa", 0, 4)

print(user1.deposit(500))
print(user1.withdraw(100))
print(user1.apply_interest())
print(user1.display_balance())
