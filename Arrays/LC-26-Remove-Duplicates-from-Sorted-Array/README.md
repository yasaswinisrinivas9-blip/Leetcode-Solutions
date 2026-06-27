# LC-26: Remove Duplicates from Sorted Array

## Problem

Given a sorted integer array `nums`, remove the duplicates **in-place** such that each unique element appears only once.

Return the number of unique elements (`k`).

---

## Approach

This problem is solved using the **Two Pointers** technique.

* **Pointer `i`** keeps track of the last unique element.
* **Pointer `j`** scans the array looking for the next unique element.

Whenever `nums[j]` is different from `nums[i]`:

1. Move `i` one step forward.
2. Copy `nums[j]` to `nums[i]`.

At the end, the first `k = i + 1` elements contain all unique values.

---

## Dry Run

### Input

```python
nums = [0,0,1,1,1,2,2,3,3,4]
```

Initially:

```text
i = 0
j = 1
```

### Step 1

```
nums[i] = 0
nums[j] = 0
```

Duplicate → Skip

```
[0,0,1,1,1,2,2,3,3,4]
 i j
```

---

### Step 2

```
j = 2

nums[i] = 0
nums[j] = 1
```

New unique element found.

Move `i` forward.

```
i = 1
nums[1] = nums[2]
```

Array becomes

```
[0,1,1,1,1,2,2,3,3,4]
    i   j
```

Unique portion:

```
[0,1]
```

---

### Step 3

```
j = 5

nums[i] = 1
nums[j] = 2
```

Move `i`

```
i = 2
nums[2] = 2
```

```
[0,1,2,1,1,2,2,3,3,4]
       i     j
```

Unique portion:

```
[0,1,2]
```

---

### Continue

When `3` is found:

```
[0,1,2,3,1,2,2,3,3,4]
```

When `4` is found:

```
[0,1,2,3,4,2,2,3,3,4]
```

---

## Final Output

```
i = 4
```

Return

```python
i + 1
```

```
5
```

The first five elements are:

```
[0,1,2,3,4]
```

---

## Intuition

Think of `i` as the **boundary of unique elements**.

Initially:

```
[0 | 0 1 1 1 2 2 3 3 4]
 i
```

After finding `1`:

```
[0 1 | 1 1 1 2 2 3 3 4]
    i
```

After finding `2`:

```
[0 1 2 | 1 1 2 2 3 3 4]
      i
```

After finding `3`:

```
[0 1 2 3 | 1 2 2 3 3 4]
        i
```

After finding `4`:

```
[0 1 2 3 4 | 2 2 3 3 4]
          i
```

Everything before `i` is unique.

---

## Time Complexity

* **O(N)**

---

## Space Complexity

* **O(1)**

---

## Pattern

* Two Pointers
* In-place Array Modification
