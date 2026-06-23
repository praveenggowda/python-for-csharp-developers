from pathlib import Path
from src import processor, storage
from src.exceptions import InsufficientFundsException, DuplicateTransactionException 

path = Path(__file__).parent / "data" / "transaction.json"

transactions = storage.load_transactions(path)
try:
    balance = processor.get_balance(transactions)
    print(balance)
except DuplicateTransactionException as e:
    print(f"Error: {e}")
except InsufficientFundsException as e:
    print(f"Error: {e}")
