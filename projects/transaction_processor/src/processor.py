from .models import Transaction
from .exceptions import InsufficientFundsException, DuplicateTransactionException, InvalidTransactionTypeException, NegativeAmountException

def process_transactions(transactions: list[Transaction]) -> float:
    seen_ids = set()
    balance = 0.0

    for transaction in transactions:
        if transaction.id in seen_ids:
            raise DuplicateTransactionException(f"Duplicate transaction: {transaction.id}")
        else:
            if transaction.amount <=0:
                raise NegativeAmountException(f"Amount must be positive")

            if transaction.transaction_type == 'deposit':
                balance += transaction.amount
            elif transaction.transaction_type == 'withdraw':
                if transaction.amount > balance:
                    raise InsufficientFundsException(f"Insufficient funds for transaction: {transaction.id}")
                
                balance -= transaction.amount
            else:
                raise InvalidTransactionTypeException(f"Unsupported transaction type: {transaction.transaction_type}")

            seen_ids.add(transaction.id)

    return balance