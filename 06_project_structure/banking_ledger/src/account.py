from dataclasses import dataclass, field

@dataclass
class Account:
    id: str
    owner: str
    balance: float = 0.0
    transactions: list = field(default_factory=list)