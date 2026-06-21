import pytest

from account import Account

def test_deposit_increase_balance():
    acc = Account("001", "Praveen", 1000.0)
    acc.deposit(500.0)
    assert acc.balance == 1500.0

def test_withdraw_decreases_balance():
    acc = Account("001", "Praveen", 1000.0)
    acc.withdraw(200.0)
    assert acc.balance == 800.0

def test_withdraw_insufficient_funds_raises_error():
    acc = Account("001", "Praveen", 1000.0)
    with pytest.raises(ValueError):
        acc.withdraw(9999.0) 
