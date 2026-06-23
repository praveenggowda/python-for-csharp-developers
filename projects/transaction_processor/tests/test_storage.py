import pytest
from src import storage
from pathlib import Path

def test_load_file_returns_transactions():
    file_path = Path(__file__).parent / "valid_transactions.json"
    transactions = storage.load_transactions(file_path)
    assert len(transactions) == 3

def test_load_empty_file_returns_empty_list():
    file_path = Path(__file__).parent / "empty_transactions.json"
    transactions = storage.load_transactions(file_path)
    assert len(transactions) == 0