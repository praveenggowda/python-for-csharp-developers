# Banking Ledger

A simple banking ledger built in Python using the standard library only.

## Features

- Deposit money into an account
- Withdraw money from an account
- Check current balance
- View full transaction statement
- View account profile

## Project Structure

```
banking_ledger/
├── src/
│   ├── models.py       # Account and Transaction dataclasses
│   └── services.py     # Business logic
├── tests/
│   └── test_services.py
├── main.py
├── requirements.txt
└── README.md
```

## Run

```bash
python3 main.py
```

## Test

```bash
python3 -m pytest tests/ -v
```
