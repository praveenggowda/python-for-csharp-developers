from src import ledger_service
from src.account import Account

acc = Account("001", "Praveen", 1000.0)
ledger_service.deposit(acc, 1000.0)
ledger_service.withdraw(acc, 200.0)
print(ledger_service.check_balance(acc))
print(ledger_service.get_profile(acc))
print(ledger_service.get_statement(acc))