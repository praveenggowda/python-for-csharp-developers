import json
from pathlib import Path
from .models import Transaction

def load_transactions(file_path: str) -> list[Transaction]:    
    with open(file_path, "r") as file:  
        data = json.load(file)
        return [Transaction(**item) for item in data]