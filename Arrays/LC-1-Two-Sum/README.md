# LC-1: Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

---

## Intuition

A brute-force solution would compare every pair of elements, resulting in **O(N²)** time complexity.

A more efficient approach is to use a **Hash Map (Dictionary)** to store previously seen numbers and their indices.

For each element:

* Compute the required complement:

  ```python
  complement = target - nums[i]
  ```

* If the complement already exists in the hash map, we have found the answer.

* Otherwise, store the current number and its index in the hash map and continue.

This allows us to find the required pair in a single traversal.

---

## Approach

1. Initialize an empty dictionary.
2. Traverse the array once.
3. For each element:

   * Calculate the complement.
   * Check if the complement exists in the dictionary.
   * If found, return the stored index and the current index.
   * Otherwise, store the current element with its index.
4. Continue until the solution is found.

---

## Example

### Input

```python
nums = [2, 7, 11, 15]
target = 9
```

### Dry Run

| Index | Value | Complement | Hash Map | Result        |
| ----: | ----: | ---------: | -------- | ------------- |
|     0 |     2 |          7 | {2:0}    | Continue      |
|     1 |     7 |          2 | {2:0}    | Found → [0,1] |

### Output

```python
[0, 1]
```

---

## Time Complexity

**O(N)**

The array is traversed only once.

---

## Space Complexity

**O(N)**

A hash map is used to store previously visited elements.

---

## Pattern

* Arrays
* Hash Map
* One Pass
* Lookup Optimization

---

## Key Takeaway

Using a hash map reduces the time complexity from **O(N²)** to **O(N)** by trading additional space for faster lookups.
