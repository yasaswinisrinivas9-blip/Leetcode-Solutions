# Sort an Array of 0s, 1s and 2s

## Problem

Given an array consisting only of **0s, 1s, and 2s**, sort the array in ascending order **in-place**.

The goal is to solve the problem without using any built-in sorting algorithm.

---

# Approach - Optimal (Dutch National Flag Algorithm)

## Intuition

The array contains only three distinct values:

- `0`
- `1`
- `2`

Instead of sorting, divide the array into four regions using three pointers.

```
0s | 1s | Unknown | 2s
```

- **low** → Position where the next `0` should be placed.
- **mid** → Current element being processed.
- **high** → Position where the next `2` should be placed.

The unknown region gradually shrinks until the entire array becomes sorted.

---

## Algorithm

1. Initialize:
   - `low = 0`
   - `mid = 0`
   - `high = n - 1`

2. While `mid <= high`:

- If `nums[mid] == 0`
  - Swap `nums[low]` and `nums[mid]`
  - Increment both `low` and `mid`

- If `nums[mid] == 1`
  - Increment `mid`

- If `nums[mid] == 2`
  - Swap `nums[mid]` and `nums[high]`
  - Decrement `high`

3. Continue until `mid > high`.

---

## Example

### Input

```python
nums = [2,0,2,1,1,0]
```

### Dry Run

Initial

```
[2,0,2,1,1,0]
 L M       H
```

Swap `2` with `0`

```
[0,0,2,1,1,2]
 L M     H
```

Move `low` and `mid`

```
[0,0,2,1,1,2]
   L M   H
```

Swap `2` with `1`

```
[0,0,1,1,2,2]
     M H
```

Continue until

```
[0,0,1,1,2,2]
```

---

## Time Complexity

**O(N)**

Each element is processed at most once.

---

## Space Complexity

**O(1)**

Sorting is performed completely in-place.

---

## Pattern

- Arrays
- Three Pointers
- Dutch National Flag Algorithm
- In-place Sorting

---

## Key Takeaway

Instead of comparing every pair of elements, maintain three pointers that divide the array into sorted regions.

This allows the array to be sorted in a **single traversal**, making it one of the most efficient in-place sorting algorithms for arrays containing only `0`, `1`, and `2`.