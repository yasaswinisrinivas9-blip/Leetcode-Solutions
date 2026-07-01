## Optimal Approach (Kadane's Algorithm)

Kadane's Algorithm finds the maximum subarray sum by maintaining a **running sum** while traversing the array.

1. Initialize:

   * `current_sum = 0`
   * `maximum_sum = nums[0]`

2. Traverse the array from left to right.

3. For each element:

   * Add the current element to `current_sum`.
   * Update `maximum_sum` if `current_sum` is greater.
   * If `current_sum` becomes negative, reset it to `0` because a negative sum cannot increase the sum of any future subarray.

4. Continue until all elements have been processed.

5. Return `maximum_sum`.

### Dry Run

Input

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

| Element | Current Sum | Maximum Sum |
| ------: | ----------: | ----------: |
|      -2 |      -2 → 0 |          -2 |
|       1 |           1 |           1 |
|      -3 |      -2 → 0 |           1 |
|       4 |           4 |           4 |
|      -1 |           3 |           4 |
|       2 |           5 |           5 |
|       1 |           6 |           6 |
|      -5 |           1 |           6 |
|       4 |           5 |           6 |

The maximum subarray is:

```text
[4, -1, 2, 1]
```

Maximum Sum:

```text
6
```
