# JSON, File I/O, pathlib, Idempotency

---

## JSON

```python
import json

json.dumps(obj)       # Python → JSON string
json.loads(text)      # JSON string → Python
json.dump(obj, file)  # Python → file
json.load(file)       # file → Python
```

Rule: `s` at the end = string. No `s` = file.

---

## pathlib

```python
from pathlib import Path

Path(__file__).parent              # current directory
Path(__file__).parent / "data.json"  # join path
```

Cross-platform. Cleaner than string concatenation.

---

## File I/O

```python
with open(path, "r") as file:   # read
    data = json.load(file)

with open(path, "w") as file:   # write
    json.dump(data, file)
```

`with open(...)` automatically closes the file — equivalent of `using` in C#.

---

## Idempotency

Processing the same request multiple times produces the same result.

```python
seen_ids = set()

if transaction_id not in seen_ids:
    # process
    seen_ids.add(transaction_id)
```

Banking example: customer submits payment TXN001 twice. First request processed. Second request ignored. Prevents duplicate payments.

Use a `set` not a `dict` — only tracking existence, not storing values.

---

## Transaction Processor Built

Features: read JSON, process deposits and withdrawals, track balance, prevent duplicate transactions via idempotency.
