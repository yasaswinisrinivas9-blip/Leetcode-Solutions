# LeetCode 15. 3Sum

## Problem
Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`
- `j != k`
- `i != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

---

## Approach

1. Sort the array.
2. Iterate through each element as the first element of the triplet.
3. Skip duplicate values to avoid repeated triplets.
4. Use the Two Pointer technique:
   - `left = i + 1`
   - `right = n - 1`
5. Calculate the sum of the three elements.
   - If the sum is `0`, store the triplet.
   - If the sum is less than `0`, move the left pointer.
   - If the sum is greater than `0`, move the right pointer.
6. Skip duplicate values for both pointers after finding a valid triplet.

---

## Algorithm

- Sort the array.
- Traverse each index `i`.
- Ignore duplicate starting elements.
- Apply the two-pointer technique to search for the remaining two numbers.
- Store every unique triplet whose sum equals zero.

---

## Time Complexity

- Sorting: **O(n log n)**
- Two Pointer Traversal: **O(n²)**

**Overall:** **O(n²)**

---

## Space Complexity

- **O(1)** (excluding the output list)

---

## Concepts Used

- Sorting
- Two Pointers
- Arrays
- Duplicate Handling