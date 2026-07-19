# Replace Elements with Greatest Element on Right Side

## Problem

Given an integer array `arr`, replace every element with the greatest element among the elements to its right. The last element should be replaced with `-1`.

## Approach

This solution traverses the array from **right to left** while maintaining the maximum element seen so far.

### Algorithm

1. Initialize `max_so_far = -1`.
2. Traverse the array from the last index to the first.
3. Store the current value.
4. Replace the current element with `max_so_far`.
5. Update `max_so_far` using the stored value.
6. Return the modified array.

## Python Solution

```python
class Solution:
    def replaceElements(self, arr):

        max_so_far = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, current)

        return arr
```

## Example

**Input**

```
arr = [17,18,5,4,6,1]
```

**Output**

```
[18,6,6,6,1,-1]
```

## Complexity Analysis

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

## Key Learning

* Reverse traversal
* Maintaining a running maximum
* In-place array modification
* Constant extra space optimization
