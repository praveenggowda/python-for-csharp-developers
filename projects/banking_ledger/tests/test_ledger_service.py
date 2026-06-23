import pytest

from src.account import Account
from src import ledger_service 
from src.exceptions import InsufficientFundsException

def test_withdraw_decreases_balance():
    acc = Account("001", "Praveen", 1000.0)
    ledger_service.withdraw(acc, 100.0)
    assert acc.balance == 900.0
    assert len(acc.transactions) == 1

def test_withdraw_insufficient_fund_raises_error(): 
    acc = Account("001", "Praveen", 100.0)
    with pytest.raises(InsufficientFundsException):
        ledger_service.withdraw(acc, 200.0)

def test_deposit_increases_balance():
    acc = Account("001", "Praveen", 100.0)
    ledger_service.deposit(acc, 100.0)
    assert acc.balance == 200.0

def test_check_balance_returns_updated_amount():
    acc = Account("001", "Praveen", 100.0)
    ledger_service.deposit(acc, 100.0)
    assert ledger_service.check_balance(acc) == 200.0

def test_get_statement_returns_all_transactions():
    acc = Account("001", "Praveen", 100.0)
    ledger_service.deposit(acc, 100.0)
    ledger_service.withdraw(acc, 10.0)
    
    statement = ledger_service.get_statement(acc)
    assert len(statement) == 2 

def test_get_profile_returns_owner():
    acc = Account("001", "Praveen", 100.0)
    assert ledger_service.get_profile(acc) == "Praveen"
