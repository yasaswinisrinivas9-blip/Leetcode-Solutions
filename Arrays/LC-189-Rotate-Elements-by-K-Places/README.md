## Intuition

Rotating the array one position at a time would require repeating the operation `k` times, resulting in an inefficient solution.

A more efficient approach is to use the **Reversal Algorithm**, which performs the rotation in-place using three array reversals.

The idea is:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n - k` elements.

This rearranges the elements into their correct rotated positions while using constant extra space.

---

## Approach

Given:

```python
nums = [1,2,3,4,5,6,7]
k = 3
```

### Step 1: Reverse the Entire Array

```text
[7,6,5,4,3,2,1]
```

### Step 2: Reverse the First `k` Elements

```text
[5,6,7,4,3,2,1]
```

### Step 3: Reverse the Remaining `n-k` Elements

```text
[5,6,7,1,2,3,4]
```

The final array is successfully rotated to the right by `k` positions.

---

## Time Complexity

**O(N)**

* Reversing the entire array takes **O(N)**.
* Reversing the first `k` elements takes **O(k)**.
* Reversing the remaining `n-k` elements takes **O(N-k)**.

Overall:

```text
O(N) + O(k) + O(N-k) = O(2N) = O(N)
```

---

## Space Complexity

**O(1)**

The rotation is performed **in-place** without using any extra array.

---

## Pattern

* Arrays
* Reversal Algorithm
* Two Pointers
* In-place Array Manipulation
