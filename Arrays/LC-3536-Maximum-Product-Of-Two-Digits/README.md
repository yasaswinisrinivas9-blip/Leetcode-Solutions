# LeetCode 3536. Maximum Product of Two Digits

## Problem

Given a positive integer `n`, return the maximum product of any two digits present in `n`.

---

## Approach

1. Convert the integer into a list of its digits.
2. Sort the digits in descending order.
3. The first two digits are the largest.
4. Return their product.

---

## Algorithm

- Convert `n` to a string.
- Convert each character back to an integer.
- Sort the digits in decreasing order.
- Multiply the first two digits.
- Return the result.

---

## Time Complexity

- Converting number to digits: **O(d)**
- Sorting digits: **O(d log d)**

**Overall:** **O(d log d)**

> `d` = Number of digits in `n` (maximum 10).

---

## Space Complexity

- **O(d)**

---

## Concepts Used

- String Conversion
- Sorting
- Arrays