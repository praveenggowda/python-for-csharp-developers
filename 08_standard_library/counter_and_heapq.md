# Counter and heapq

---

## Counter

```python
from collections import Counter

frequencies = Counter(nums)
```

Example:

```python
nums = [1, 1, 1, 2, 2, 3]
Counter(nums)
# {1: 3, 2: 2, 3: 1}
```

Counter = Dictionary + automatic frequency counting. Eliminates manual boilerplate:

```python
# Manual equivalent
frequencies = {}
for num in nums:
    frequencies[num] = frequencies.get(num, 0) + 1
```

---

## Dictionary .items()

```python
frequencies.items()
# [(1, 3), (2, 2), (3, 1)]  — (key, value) pairs
```

```csharp
// C# equivalent
foreach (var kvp in dictionary)
{
    kvp.Key;
    kvp.Value;
}
```

---

## Tuple Unpacking

```python
for num, frequency in frequencies.items():
    # num = 1, frequency = 3 on first iteration
```

Python automatically unpacks the tuple into named variables. No need to access `pair[0]` and `pair[1]`.

---

## heapq (Min Heap)

```python
import heapq

heap = []
heapq.heappush(heap, item)   # push
heapq.heappop(heap)          # pop smallest
```

Python `heapq` is a **min heap** by default — smallest element is always at the top.

---

## Heap Ordering — Critical

Heap compares tuple elements left to right. Order matters:

```python
# Wrong — heap sorts by num, not frequency
heapq.heappush(heap, (num, frequency))

# Correct — heap sorts by frequency first
heapq.heappush(heap, (frequency, num))
```

**Rule:** put the value you want to sort by first.

---

## Min Heap of Size K Pattern

```python
for num, frequency in Counter(nums).items():
    heapq.heappush(heap, (frequency, num))

    if len(heap) > k:
        heapq.heappop(heap)  # removes lowest frequency
```

Push first, pop second. This keeps only the top K elements in the heap.

```python
# Wrong order — removes the item you just added
if len(heap) == k:
    heapq.heappop(heap)
heapq.heappush(heap, item)
```

---

## Key Takeaways

- `Counter(nums)` replaces manual frequency counting
- `.items()` gives `(key, value)` pairs — use tuple unpacking
- `heapq` is min heap — lowest value at top
- Always store `(frequency, num)` not `(num, frequency)`
- Push first, pop second when maintaining heap of size K
