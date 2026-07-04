# LC-27: Remove Element

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**.

Return the number of elements remaining after the removal.

The relative order of the remaining elements may be changed.

---

## Intuition

Instead of creating a new array, we can overwrite the elements that should be kept.

Use two pointers:

- **Read Pointer (`i`)** → Traverses the array.
- **Write Pointer (`k`)** → Indicates where the next valid element should be placed.

Whenever an element is **not equal** to `val`, copy it to index `k` and increment `k`.

After traversing the array, the first `k` elements contain the required answer.

---

## Approach

1. Initialize `k = 0`.
2. Traverse the array using pointer `i`.
3. If `nums[i]` is not equal to `val`:
   - Copy `nums[i]` to `nums[k]`.
   - Increment `k`.
4. Continue until the end of the array.
5. Return `k`.

---

## Example

### Input

```python
nums = [3,2,2,3]
val = 3
```

### Dry Run

| Read Pointer (`i`) | Element | Write Pointer (`k`) | Array |
|-------------------:|--------:|--------------------:|-------|
| 0 | 3 | 0 | Skip |
| 1 | 2 | 0 | [2,2,2,3] |
| 2 | 2 | 1 | [2,2,2,3] |
| 3 | 3 | 2 | Skip |

### Output

```python
2
```

Remaining elements:

```text
[2,2]
```

---

## Time Complexity

**O(N)**

The array is traversed only once.

---

## Space Complexity

**O(1)**

The array is modified in-place without using additional memory.

---

## Pattern

- Arrays
- Two Pointers
- In-place Array Modification

---

## Key Takeaway

The **Read Pointer** scans every element, while the **Write Pointer** keeps track of where the next valid element should be stored.

This allows the problem to be solved in **O(N)** time with **O(1)** extra space.