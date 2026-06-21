# Python OOP for C# Developers

---

## Classes

```python
# Create class
class Account:
    pass

# Constructor
def __init__(self, id: str, owner: str, balance: float):
    self.id = id
    self.owner = owner
    self.balance = balance

# Create object
account = Account("001", "Praveen", 1000)
```

`self` in Python = `this` in C#. Always the first parameter of every method.

---

## Methods

```python
def deposit(self, amount: float):
    self.balance += amount
```

```csharp
// C# equivalent
public void Deposit(decimal amount)
{
    Balance += amount;
}
```

---

## Exceptions

```python
raise Exception("Something went wrong")     # generic — avoid
raise ValueError("Invalid input")           # specific — prefer this

try:
    account.withdraw(9999)
except ValueError as ex:
    print(ex)
```

```csharp
// C# equivalent
throw new InvalidOperationException("Insufficient funds");

try { ... }
catch (Exception ex) { Console.WriteLine(ex.Message); }
```

---

## __repr__

```python
def __repr__(self) -> str:
    return f"Account(id={self.id}, owner={self.owner}, balance={self.balance})"
```

```csharp
// C# equivalent
public override string ToString()
{
    return $"Account(Id={Id}, Owner={Owner}, Balance={Balance})";
}
```

Without `__repr__`, `print(account)` shows `<__main__.Account object at 0x...>`.

---

## @dataclass

```python
from dataclasses import dataclass

@dataclass
class Account:
    id: str
    owner: str
    balance: float
```

Automatically generates: `__init__`, `__repr__`, `__eq__`.

```csharp
// C# equivalent
public record Account(string Id, string Owner, decimal Balance);
```

**When to use:**
- Simple data container → `@dataclass`
- Complex logic, custom init, inheritance → normal class
