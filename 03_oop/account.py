class Account:
    def __init__(self, id: str, owner: str, balance: float):
        self.id = id
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float): 
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __repr__(self) -> str:
        return f"Account(id={self.id}, owner={self.owner}, balance={self.balance})"
    
acc = Account("001", "Praveen", 1000.0)
acc.deposit(500)
acc.withdraw(200)
print(acc)