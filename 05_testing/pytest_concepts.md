# pytest Concepts

---

## Imports

```python
import pytest
from account_dataclass import AccountDataClass
```

```csharp
// C# equivalent
using MyProject.AccountDataClass;
```

---

## Test Naming Convention

```python
def test_deposit_increase_balance():
def test_deposit_decrease_balance():
def test_withdraw_insufficient_funds_raises_error():
```

All test functions must start with `test_` — pytest discovers them automatically.

---

## Arrange Act Assert

```python
def test_deposit_increase_balance():
    # Arrange
    acc = AccountDataClass("001", "Praveen", 100.0)

    # Act
    acc.deposit(200.0)

    # Assert
    assert acc.balance == 300.0
```

---

## Assertions

```python
assert acc.balance == 300.0
```

```csharp
// C# equivalent
Assert.AreEqual(300.0, acc.Balance);
```

---

## Exception Testing

```python
with pytest.raises(ValueError):
    acc.withdraw(200.0)
```

```csharp
// C# equivalent
Assert.Throws<ValueError>(() => acc.Withdraw(200.0));
```

If the exception is not thrown, the test fails.

---

## Test Independence

Each test creates its own object — tests can run in any order and do not affect each other.

```python
def test_x():
    acc = AccountDataClass(...)

def test_y():
    acc = AccountDataClass(...)
```

---

## pytest Commands

```bash
pytest                            # run all tests
pytest -v                         # verbose
pytest --cov                      # coverage
pytest --cov-report=term-missing  # show missing lines
```

---

## Key Rules

1. Functions starting with `test_` are auto-discovered
2. `assert` is the primary assertion mechanism
3. `pytest.raises()` verifies exceptions
4. Follow Arrange → Act → Assert
5. Tests must be independent
6. Test behaviour, not implementation
7. Dataclasses can be tested exactly like normal classes

---

## Thought Machine Takeaway

Production-quality code requires type hints, error handling, unit tests, and clear naming. A solution with tests is significantly stronger than one without. Testing is a first-class engineering skill, not an optional extra.
