from dataclasses import dataclass 

@dataclass
class AccountDataClass:
    id: str
    owner: str
    balance: float

    def deposit(self, amount: float): 
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

acc = AccountDataClass("001", "Praveen Girish", 1000.0)
acc.deposit(500)
acc.withdraw(200)
print(acc)
