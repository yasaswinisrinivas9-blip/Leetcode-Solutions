# LC-485: Max Consecutive Ones

## Problem

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

---

## Intuition

The longest sequence of consecutive `1`s can be found by traversing the array once while maintaining two variables:

* `current_count` → Counts the current consecutive `1`s.
* `max_count` → Stores the maximum consecutive `1`s found so far.

Whenever a `1` is encountered, increment the current count.

Whenever a `0` is encountered, update the maximum count (if needed) and reset the current count.

---

## Approach

1. Initialize:

   * `current_count = 0`
   * `max_count = 0`
2. Traverse the array.
3. If the current element is `1`:

   * Increment `current_count`.
   * Update `max_count`.
4. Otherwise:

   * Reset `current_count` to `0`.
5. Return `max_count`.

---

## Example

### Input

```python
nums = [1,1,0,1,1,1]
```

### Dry Run

| Element | Current Count | Maximum Count |
| ------- | ------------: | ------------: |
| 1       |             1 |             1 |
| 1       |             2 |             2 |
| 0       |             0 |             2 |
| 1       |             1 |             2 |
| 1       |             2 |             2 |
| 1       |             3 |             3 |

### Output

```python
3
```

---

## Time Complexity

**O(N)**

The array is traversed exactly once.

---

## Space Complexity

**O(1)**

Only two integer variables are used.

---

## Pattern

* Arrays
* Linear Traversal
* Counting

---

## Key Takeaway

Maintain a running count of consecutive `1`s and reset it whenever a `0` is encountered.

Track the maximum count throughout the traversal to obtain the answer in **O(N)** time using **O(1)** extra space.
