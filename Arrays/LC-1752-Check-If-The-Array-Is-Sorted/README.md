# LC-1752: Check if Array Is Sorted and Rotated

## Problem

Given an array `nums`, return `true` if the array was originally sorted in non-decreasing order and then rotated some number of positions (including zero). Otherwise, return `false`.

---

## Intuition

A sorted and rotated array has **at most one position** where the order decreases.

For example:

```text id="nbibqq"
[3,4,5,1,2]
```

There is only one decreasing pair:

```text id="1n1twg"
5 > 1
```

If an array has more than one such decreasing pair, it cannot be obtained by rotating a sorted array.

Additionally, since the array is circular, compare the **last element with the first element**.

---

## Approach

1. Initialize a counter `count = 0`.
2. Traverse the array.
3. Compare each element with the next element using circular indexing:

```python id="qol8dv"
nums[i] > nums[(i + 1) % n]
```

4. If the current element is greater than the next element, increment `count`.
5. If `count` becomes greater than `1`, return `False`.
6. Otherwise, return `True`.

---

## Example 1

### Input

```python id="4ot8sy"
nums = [3,4,5,1,2]
```

Comparisons

```text id="rrj6m3"
3 < 4 ✅
4 < 5 ✅
5 > 1 ❌ (count = 1)
1 < 2 ✅
2 < 3 ✅
```

Output

```python id="o9czzj"
True
```

---

## Example 2

### Input

```python id="kls5tw"
nums = [2,1,3,4]
```

Comparisons

```text id="5g7lqn"
2 > 1 ❌ (count = 1)
1 < 3 ✅
3 < 4 ✅
4 > 2 ❌ (count = 2)
```

Since there are two decreasing pairs:

Output

```python id="psdv8q"
False
```

---

## Time Complexity

**O(N)**

The array is traversed only once.

---

## Space Complexity

**O(1)**

Only a counter variable is used.

---

## Pattern

* Arrays
* Circular Traversal
* Simulation

---

## Key Takeaway

A sorted and rotated array can contain **at most one inversion (decreasing pair)**.

By counting these inversions during a single traversal, we can determine the answer efficiently in **O(N)** time using **O(1)** extra space.
