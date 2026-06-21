# Day 1 — Two Sum and Python Fundamentals

## Problem

Given an array of integers and a target value, return the indices of two numbers that add up to the target.

---

## 1. enumerate() vs range()

Use `enumerate()` when you need both the index and the value.

```python
for i, num in enumerate(nums):
    print(i, num)
```

Use `range()` when you only need the index.

```python
for i in range(len(nums)):
    print(i)
```

**C# equivalent:**
```csharp
for (int i = 0; i < nums.Length; i++)
{
    int num = nums[i];
}
```

**Rule:** need index and value → `enumerate()`. Need only index → `range()`.

---

## 2. Dictionary (HashMap)

```python
seen = {}              # Create — C#: var seen = new Dictionary<int, int>()
seen[num] = i          # Add    — C#: seen[num] = i
if complement in seen  # Check  — C#: seen.ContainsKey(complement)
seen[complement]       # Get    — C#: seen[complement]
```

Average lookup time: O(1)

---

## 3. Function Signature

```python
# Without type hints
def two_sum(nums, target):

# With type hints (recommended)
def two_sum(nums: list[int], target: int) -> list[int]:
```

**C# equivalent:**
```csharp
int[] TwoSum(int[] nums, int target)
```

Python uses dynamic typing so type hints are optional but recommended for production code.

---

## 4. HashMap Pattern

For each number:
1. Calculate complement = target - num
2. Check if complement already exists in dict
3. If yes, return both indices
4. Otherwise store current number and index

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
```

---

## Complexity

| | Brute Force | Optimised |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(n) |

---

## Interview Takeaway

Two Sum teaches:
- Dictionaries as HashMaps
- `enumerate()` over `range(len())`
- One-pass lookup pattern
- Trading space for time — O(n) space to get O(n) time
