from .account import Account
from .transaction import Transaction
from .exceptions import InsufficientFundsException

def withdraw(account: Account, amount: float):
    if amount > account.balance:
        raise InsufficientFundsException("Insufficient funds")
    
    account.balance -= amount
    transaction = Transaction(amount, f"Withdrawn £{amount} successfully")
    account.transactions.append(transaction)

def deposit(account: Account, amount: float):
    account.balance += amount
    transaction = Transaction(amount, f"Deposited £{amount} successfully")
    account.transactions.append(transaction)

def check_balance(account: Account) -> float:
    return account.balance

def get_statement(account: Account) -> list:
    return account.transactions

def get_profile(account: Account) -> str:
    return account.owner