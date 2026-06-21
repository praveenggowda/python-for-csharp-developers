# Python Concepts for C# Developers

---

## Functions

```python
# Basic
def two_sum(nums, target):

# With type hints
def two_sum(nums: list[int], target: int) -> list[int]:
```

```csharp
// C# equivalent
int[] TwoSum(int[] nums, int target)
```

---

## Lists

```python
nums = [1, 2, 3]       # Create       — C#: var nums = new List<int> {1,2,3}
nums.append(4)          # Add          — C#: nums.Add(4)
nums.pop(2)             # Remove index — C#: nums.RemoveAt(2)
len(nums)               # Length       — C#: nums.Count
```

### List Slicing

```python
nums[-1]     # Last element
nums[-2]     # Second last
nums[:3]     # First three
nums[3:]     # From index 3 onwards
nums[1:4]    # Between index 1 and 4
nums[1:]     # Skip first element (used in Kadane's)
```

---

## Dictionaries

```python
seen = {}                    # Create — C#: new Dictionary<int, int>()
seen: dict[int, int] = {}   # With type hint
seen[num] = index            # Add
seen[num]                    # Lookup
if num in seen:              # Check  — C#: seen.ContainsKey(num)
```

---

## Sets

```python
seen = set()     # Create  — C#: new HashSet<int>()
seen.add(num)    # Add     — C#: seen.Add(num)
if num in seen:  # Contains — C#: seen.Contains(num)
```

---

## enumerate() vs range()

```python
# Need index + value
for i, num in enumerate(nums):   # C#: for(int i = 0; i < nums.Length; i++)

# Need only index
for i in range(len(nums)):
```

**Rule:** need index and value → `enumerate()`. Need only index → `range()`.

---

## Fixed Size Arrays

```python
count = [0] * 26   # C#: int[] count = new int[26]
```

Used for: Valid Anagram, character counting, lowercase English letters problems.

---

## Character to Index

```python
ord(c) - ord('a')   # C#: c - 'a'
ord('c') - ord('a') # Returns 2
```

---

## String Sorting

```python
sorted(word)              # Returns ['a', 'e', 't']
''.join(sorted(word))     # Returns "aet"
```

All anagrams produce the same sorted string. Used as dictionary key in Group Anagrams.

---

## Tuple

```python
key = tuple(count)   # Immutable — can be used as dict key
```

Lists cannot be dict keys (mutable). Tuples can (immutable).

---

## defaultdict

```python
from collections import defaultdict

groups = defaultdict(list)
groups[key].append(word)   # No need to check if key exists
```

```python
# Without defaultdict
if key not in groups:
    groups[key] = []
groups[key].append(word)
```

```csharp
// C# equivalent
if (!dict.ContainsKey(key))
    dict[key] = new List<string>();
dict[key].Add(value);
```

---

## min() and max()

```python
min(a, b)    # C#: Math.Min(a, b)
max(a, b)    # C#: Math.Max(a, b)

min_price = min(min_price, price)
max_profit = max(max_profit, profit)
```

---

## Infinity Values

```python
float('inf')    # C#: int.MaxValue
float('-inf')   # C#: int.MinValue
```

---

## Division

```python
13 / 5    # 2.6  — normal division
13 // 5   # 2    — floor division
int(a / b)  # truncates toward zero (used in Reverse Polish Notation)
```

---

## Current Python Toolkit

Comfortable with: functions, type hints, lists, dicts, sets, `enumerate()`, `range()`, `ord()`, fixed arrays, string sorting, `defaultdict`, `min()`/`max()`, list slicing, tuple, greedy, Kadane's.

## Next Topics

`Counter`, Top K Frequent Elements, `deque`, classes, dataclasses, exception handling, pytest, project structure, FastAPI.

**Goal:** stop translating from C#, start thinking naturally in Python.
