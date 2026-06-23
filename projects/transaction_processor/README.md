# Transaction Processor

A production-quality transaction processor built in Python using the standard library only.

## Features

- Process deposits and withdrawals
- Enforce idempotency — duplicate transaction IDs are rejected
- Validate business rules — insufficient funds raise an exception
- Validate transaction types — unsupported types are rejected
- Validate amounts — negative or zero amounts are rejected

## Project Structure

```
transaction_processor/
├── src/
│   ├── models.py       # Transaction dataclass
│   ├── processor.py    # Business logic
│   ├── storage.py      # JSON file reading
│   └── exceptions.py   # Custom exceptions
├── tests/
│   ├── test_processor.py
│   └── test_storage.py
├── data/
│   └── transactions.json
├── main.py
└── requirements.txt
```

## Run

```bash
python3 main.py
```

## Test

```bash
python3 -m pytest tests/ -v
```

## Business Rules

| Rule | Behaviour |
|---|---|
| Duplicate transaction ID | Raises `DuplicateTransactionException` |
| Withdrawal exceeds balance | Raises `InsufficientFundsException` |
| Unknown transaction type | Raises `InvalidTransactionTypeException` |
| Negative or zero amount | Raises `NegativeAmountException` |
