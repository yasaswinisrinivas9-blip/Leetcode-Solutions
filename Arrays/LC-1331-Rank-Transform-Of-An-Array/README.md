# 1331. Rank Transform of an Array

## Problem

Given an integer array `arr`, replace each element with its **rank**.

### Rank Rules

* Rank starts from **1**.
* Larger elements have larger ranks.
* Equal elements have the **same rank**.
* Ranks should be as small as possible.

---

## Approach

1. Remove duplicate elements using a `set`.
2. Sort the unique elements.
3. Assign a rank to each unique element using a dictionary.
4. Traverse the original array and replace every element with its assigned rank.

---

## Algorithm

1. Create a sorted list of unique elements.
2. Initialize an empty dictionary `rank`.
3. Assign ranks starting from `1`.
4. Replace every element in the original array using the dictionary.
5. Return the transformed array.

---

## Python Solution

```python
class Solution:
    def arrayRankTransform(self, arr: List[int]):

        sorted_arr = sorted(set(arr))

        rank = {}
        r = 1

        for num in sorted_arr:
            rank[num] = r
            r += 1

        return [rank[num] for num in arr]
```

---

## Example

### Input

```text
arr = [40,10,20,30]
```

### Sorted Unique Elements

```text
[10,20,30,40]
```

### Rank Mapping

```text
10 → 1
20 → 2
30 → 3
40 → 4
```

### Output

```text
[4,1,2,3]
```

---

## Time Complexity

* Creating set: **O(n)**
* Sorting unique elements: **O(n log n)** (worst case)
* Assigning ranks: **O(n)**
* Replacing elements: **O(n)**

**Overall Time Complexity:** **O(n log n)**

---

## Space Complexity

* Set: **O(n)**
* Sorted array: **O(n)**
* Dictionary: **O(n)**

**Overall Space Complexity:** **O(n)**

---

## Key Concepts

* Sorting
* Hash Map (Dictionary)
* Set
* Array Traversal
