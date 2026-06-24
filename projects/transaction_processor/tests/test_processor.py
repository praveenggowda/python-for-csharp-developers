import pytest
from src import processor
from src.models import Transaction
from src.exceptions import InsufficientFundsException, DuplicateTransactionException, InvalidTransactionTypeException, NegativeAmountException

def test_get_balance_for_empty_list_returns_zero():
    transactions = []
    balance = processor.process_transactions(transactions)
    assert balance == 0

def test_get_balance_for_valid_transactions():
    transactions = [
        Transaction(id="TXN001", account_id="001", transaction_type="deposit", amount=100.0),
        Transaction(id="TXN002", account_id="001", transaction_type="withdraw", amount=30.0),
        Transaction(id="TXN003", account_id="001", transaction_type="withdraw", amount=50.0)
    ]
    balance = processor.process_transactions(transactions)
    assert balance == 20

def test_get_balance_duplicate_transactions_raise_exception():
    transactions = [
        Transaction(id="TXN001", account_id="001", transaction_type="deposit", amount=100.0),
        Transaction(id="TXN002", account_id="001", transaction_type="withdraw", amount=30.0),
        Transaction(id="TXN001", account_id="001", transaction_type="deposit", amount=50.0)
    ]
    with pytest.raises(DuplicateTransactionException):
        processor.process_transactions(transactions)

def test_get_balance_invalid_transaction_type_raise_exception():
    transactions = [
        Transaction(id="TXN001", account_id="001", transaction_type="deposit", amount=100.0),
        Transaction(id="TXN002", account_id="001", transaction_type="withdraw", amount=30.0),
        Transaction(id="TXN003", account_id="001", transaction_type="banana", amount=50.0)
    ]
    with pytest.raises(InvalidTransactionTypeException):
        processor.process_transactions(transactions)

def test_get_balance_negative_amount_raise_exception():
    transactions = [
        Transaction(id="TXN001", account_id="001", transaction_type="deposit", amount=100.0),
        Transaction(id="TXN002", account_id="001", transaction_type="withdraw", amount=-30.0)
    ]
    with pytest.raises(NegativeAmountException):
        processor.process_transactions(transactions)

def test_get_balance_insufficient_fund_raise_exception():
    transactions = [
        Transaction(id="TXN001", account_id="001", transaction_type="deposit", amount=10.0),
        Transaction(id="TXN002", account_id="001", transaction_type="withdraw", amount=30.0),
        Transaction(id="TXN003", account_id="001", transaction_type="deposit", amount=10.0)
    ]
    with pytest.raises(InsufficientFundsException):
        processor.process_transactions(transactions)

def test_get_balance_increases_for_deposit_transactions():
    transactions = [
        Transaction(id="TXN001", account_id="001", transaction_type="deposit", amount=100.0),
        Transaction(id="TXN002", account_id="001", transaction_type="deposit", amount=30.0)
    ]
    balance = processor.process_transactions(transactions)
    assert balance == 130

def test_get_balance_decreases_for_withdraw_transactions():
    transactions = [
        Transaction(id="TXN001", account_id="001", transaction_type="deposit", amount=100.0),
        Transaction(id="TXN002", account_id="001", transaction_type="withdraw", amount=30.0)
    ]
    balance = processor.process_transactions(transactions)
    assert balance == 70
