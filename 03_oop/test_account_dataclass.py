import pytest

from account_dataclass import AccountDataClass

def test_deposit_increase_balance():
    acc = AccountDataClass("001", "Praveen Girish", 100.0)
    acc.deposit(200.0)
    assert acc.balance == 300.0

def test_deposit_decrease_balance():
    acc = AccountDataClass("001", "Praveen Girish", 500.0)
    acc.withdraw(200.0)
    assert acc.balance == 300.0

def test_withdraw_insufficient_funds_raises_error():
    acc = AccountDataClass("001", "Praveen Girish", 100.0)
    with pytest.raises(ValueError):
        acc.withdraw(200.0)