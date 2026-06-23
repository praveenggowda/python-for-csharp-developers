# Python Learning Journey

Background: Senior Software Engineer with 14 years of experience. Primary stack: C#, .NET, AWS.

Learning Python for Thought Machine take-home challenge, Python interviews, AI agent engineering, and backend development.

Goal: Become comfortable writing Python without translating every line from C#.

---

## Functions

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    pass
```

```csharp
int[] TwoSum(int[] nums, int target)
```

---

## Lists

```python
nums = [1, 2, 3]
len(nums)        # length
nums[0]          # first element
nums[-1]         # last element
nums[-2]         # second last
nums[1:4]        # slice
nums[:3]         # from start
nums[3:]         # to end
```

---

## Dictionaries

```python
seen = {}            # create
seen[num] = index    # add
seen[num]            # lookup
if num in seen:      # check
```

```csharp
// C# equivalent
Dictionary<TKey, TValue>
```

Lookup: O(1)

---

## Sets

```python
seen = set()      # create
seen.add(num)     # add
if num in seen:   # check
```

Use case: Contains Duplicate

---

## enumerate

Use when index and value are both needed.

```python
for i, num in enumerate(nums):
```

```csharp
for(int i = 0; i < nums.Length; i++)
```

Rule: need index + value → `enumerate()`, need only index → `range()`

---

## range

```python
for i in range(len(nums)):
```

---

## Fixed Size Arrays

```python
count = [0] * 26
```

```csharp
int[] count = new int[26];
```

Used for lowercase letters and frequency counting.

---

## ord

Convert character to ASCII value.

```python
ord('a')              # returns 97
ord('c') - ord('a')   # returns 2
```

Used in: Valid Anagram

---

## Counter

```python
from collections import Counter

Counter([1,1,1,2,2,3])
# {1: 3, 2: 2, 3: 1}
```

Creates frequency map automatically.

Manual equivalent:
```python
frequencies = {}
for num in nums:
    if num not in frequencies:
        frequencies[num] = 0
    frequencies[num] += 1
```

---

## defaultdict

```python
from collections import defaultdict

groups = defaultdict(list)
groups[key].append(value)
```

Automatically creates missing lists. Without it:
```python
if key not in groups:
    groups[key] = []
groups[key].append(value)
```

---

## heapq

```python
import heapq

heap = []
heapq.heappush(heap, item)
heapq.heappop(heap)
```

Python heapq is a Min Heap.

### Heap Pattern — Top K

```python
for item in items:
    heapq.heappush(heap, item)
    if len(heap) > k:
        heapq.heappop(heap)
```

Used in: Top K Frequent Elements

---

## Tuples

```python
pair = (3, 1)
pair[0]   # 3
pair[1]   # 1

for num, frequency in frequencies.items():  # unpacking
```

---

## Dictionary Items

```python
for num, frequency in frequencies.items():  # (key, value) pairs
```

```csharp
foreach(var kvp in dictionary)
```

---

## min and max

```python
min(a, b)
max(a, b)
```

```csharp
Math.Min(a, b)
Math.Max(a, b)
```

---

## Infinity

```python
float('-inf')   # equivalent of int.MinValue
float('inf')    # equivalent of int.MaxValue
```

---

## Classes

```python
class Account:
    def __init__(self, id: str, owner: str, balance: float):
        self.id = id
        self.owner = owner
        self.balance = balance

account = Account("001", "Praveen", 1000)
```

`self` = `this` in C#. Always the first parameter of every method.

---

## Methods

```python
def deposit(self, amount: float):
    self.balance += amount
```

---

## \_\_repr\_\_

```python
def __repr__(self):
    return f"Account(id={self.id}, owner={self.owner})"
```

```csharp
public override string ToString()
```

Called automatically by `print(obj)`.

---

## Dataclasses

```python
from dataclasses import dataclass

@dataclass
class Account:
    id: str
    owner: str
    balance: float
```

Automatically generates `__init__`, `__repr__`, `__eq__`.

```csharp
public record Account(string Id, string Owner, decimal Balance);
```

When to use: simple data container → `@dataclass`, complex logic or custom init → normal class.

---

## Exceptions

```python
raise ValueError("Invalid input")

try:
    ...
except Exception as ex:
    print(ex)

class InsufficientFundsException(Exception):
    pass
```

---

## pytest

```bash
pip install pytest
pytest
pytest -v
pytest --cov
pytest --cov-report=term-missing
```

### Test Naming

```python
def test_deposit_increases_balance():
    ...
```

Convention: `test_<behaviour>`

### Assertions

```python
assert acc.balance == 1500
```

```csharp
Assert.AreEqual(...)
```

### Exception Testing

```python
with pytest.raises(ValueError):
    acc.withdraw(1001)
```

```csharp
Assert.Throws<ExceptionType>()
```

### Arrange Act Assert

```python
def test_deposit_increases_balance():
    # Arrange
    acc = Account("001", "Praveen", 1000.0)

    # Act
    acc.deposit(100.0)

    # Assert
    assert acc.balance == 1100.0
```

---

## Virtual Environment

```bash
python3 -m venv .venv       # create
source .venv/bin/activate   # activate
deactivate                  # deactivate
```

Project-specific Python environment — equivalent of NuGet restore per project.

---

## requirements.txt

```bash
pip install pytest
pip freeze > requirements.txt       # save
pip install -r requirements.txt     # install
```

---

## Project Structure

```
banking_ledger/
├── src/
│   ├── __init__.py
│   ├── account.py          # Account dataclass
│   ├── transaction.py      # Transaction dataclass
│   ├── exceptions.py       # Custom exceptions
│   └── ledger_service.py   # Business logic
├── tests/
│   ├── __init__.py
│   └── test_ledger_service.py
├── README.md
├── requirements.txt
└── main.py
```

| Python | .NET equivalent |
|---|---|
| `src/` | production project |
| `tests/` | test project |
| `main.py` | `Program.cs` |
| `requirements.txt` | `.csproj` / NuGet |
| `__init__.py` | makes folder importable as a package |

---

## DSA Problems Completed

| Problem | Pattern |
|---|---|
| Two Sum | HashMap |
| Valid Anagram | Fixed Array / Counter |
| Contains Duplicate | HashSet |
| Group Anagrams | HashMap + sort |
| Top K Frequent Elements | Heap |
| Best Time to Buy and Sell Stock | Greedy |
| Maximum Subarray | Kadane's Algorithm |

---

## JSON

Four methods. Rule: `s` at the end = string. No `s` = file.

```python
import json

json.loads('{"name": "Praveen"}')   # string → dict
json.dumps({"name": "Praveen"})     # dict → string
json.load(file)                     # file → dict
json.dump(data, file)               # dict → file
```

```csharp
// C# equivalent
JsonSerializer.Deserialize<T>(jsonString)   // → loads
JsonSerializer.Serialize(obj)               // → dumps
```

JSON uses double quotes `"`. Python dict uses single quotes `'`. Same data, different representation.

---

## pathlib

Use `pathlib` to build file paths relative to the current file — works regardless of where you run from.

```python
from pathlib import Path

path = Path(__file__).parent / "account.json"
```

`__file__` = current file. `.parent` = its folder. `/ "filename"` = joins the path.

```csharp
// C# equivalent
Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "account.json")
```

---

## File I/O

```python
# write
with open(path, "w") as file:
    json.dump(data, file)

# read
with open(path, "r") as file:
    data = json.load(file)
```

`with open(...)` automatically closes the file — equivalent of `using` in C#.

| Mode | Meaning |
|---|---|
| `"r"` | read |
| `"w"` | write (overwrites) |
| `"a"` | append |

---

## Idempotency Pattern

Reject duplicate transaction IDs using a set.

```python
seen_ids = set()

for transaction in transactions:
    if transaction['id'] not in seen_ids:
        # process
        seen_ids.add(transaction['id'])
```

Use a `set` not a `dict` — only need to track existence, not store values.

---

## Standard Library Learned

`Counter`, `defaultdict`, `heapq`, `dataclasses`, `typing`, `pytest`, `venv`, `json`, `pathlib`

---

## Applications Built

### Banking Ledger

Features: Account model, Transaction model, custom exception, deposit, withdraw, balance check, statement retrieval, unit tests, virtual environment.

Test result: 6 passed.

### Transaction Processor

Features: Read transactions from JSON, idempotency (reject duplicate IDs), deposit/withdraw logic, final balance calculation.

---

## Current Level

Comfortable with: functions, lists, dicts, sets, enumerate, range, Counter, defaultdict, heapq, classes, dataclasses, exceptions, pytest, project structure, virtual environments, JSON, pathlib, file I/O, idempotency.

Need more practice: deque, stack problems, production project design, standard library HTTP server.

---

## Next Topics

1. Valid Parentheses (Stack / deque)
2. deque patterns
3. Production Transaction Processor (proper structure, models, tests)
4. Standard library HTTP server
