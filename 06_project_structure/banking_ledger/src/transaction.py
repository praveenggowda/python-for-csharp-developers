from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Transaction:
    amount: float
    description: str
    timestamp: datetime = field(default_factory=datetime.now)