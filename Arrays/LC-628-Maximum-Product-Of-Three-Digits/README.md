# LeetCode 628 - Maximum Product of Three Numbers

## 📌 Problem
Given an integer array `nums`, return the maximum product that can be obtained by multiplying any **three numbers**.

### Example

Input:
nums = [1,2,3,4]

Output:
24

Explanation:
The maximum product is:
2 × 3 × 4 = 24

---

## 💡 Approach

1. Sort the array in ascending order.
2. There are only two possible candidates for the maximum product:
   - Product of the **three largest numbers**.
   - Product of the **two smallest (most negative) numbers** and the **largest positive number**.
3. Return the larger of the two products.

### Why consider the two smallest numbers?

Two negative numbers multiply to form a positive number.

Example:

nums = [-10, -10, 5, 2]

Three largest:
2 × 5 × (-10) = -100

Two smallest + largest:
(-10) × (-10) × 5 = 500

Maximum Product = 500

---

## ✅ Python Solution

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        nums.sort()

        product1 = nums[-1] * nums[-2] * nums[-3]

        product2 = nums[0] * nums[1] * nums[-1]

        return max(product1, product2)