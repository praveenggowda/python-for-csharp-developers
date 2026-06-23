from dataclasses import dataclass

@dataclass
class Transaction:
    id: str
    account_id: str
    transaction_type: str
    amount: float

