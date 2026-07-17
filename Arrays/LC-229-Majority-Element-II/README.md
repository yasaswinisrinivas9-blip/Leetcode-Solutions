# Majority Element II (LeetCode 229)

## 📌 Problem Statement

Given an integer array `nums`, return all elements that appear more than `⌊n / 3⌋` times.

You must solve the problem in **O(n)** time complexity and **O(1)** extra space.

---

## 🚀 Approach

This solution uses the **Boyer-Moore Voting Algorithm (Extended Version)**.

Since an element must appear more than `n/3` times, there can be **at most two majority elements**.

The algorithm works in two phases:

### Phase 1: Find Potential Candidates
- Maintain two candidates (`ele1`, `ele2`) and their respective counters (`cnt1`, `cnt2`).
- Traverse the array once.
- Update candidates and counters according to Boyer-Moore voting rules.
- Cancel out different elements by decreasing both counters whenever a new unrelated element appears.

### Phase 2: Verify Candidates
The first phase only finds **possible** majority elements.

Traverse the array again to count the occurrences of the two candidates.

Return only those whose frequency is greater than `⌊n/3⌋`.

---

## 🧠 Algorithm

1. Initialize two candidates and two counters.
2. Iterate through the array:
   - Assign candidates when counters become zero.
   - Increment the corresponding counter if the current number matches a candidate.
   - Otherwise, decrement both counters.
3. Count the actual occurrences of both candidates.
4. Return the candidates appearing more than `⌊n/3⌋` times.

---

## ✅ Time Complexity

- Candidate Selection: **O(n)**
- Verification: **O(n)**

**Overall:** `O(n)`

---

## ✅ Space Complexity

Only four variables are used regardless of input size.

**Space:** `O(1)`

---

## Example

### Input

```python
nums = [3,2,3]
```

### Output

```python
[3]
```

---

### Input

```python
nums = [1]
```

### Output

```python
[1]
```

---

### Input

```python
nums = [1,2]
```

### Output

```python
[1,2]
```

---

## 💡 Key Insight

Unlike the standard Majority Element problem (`> n/2`), where only one majority element can exist, for the `> n/3` condition there can be **at most two majority elements**.

This observation makes the extended Boyer-Moore Voting Algorithm possible.

---

## Topics

- Array
- Boyer-Moore Voting Algorithm
- Greedy
- Hashing
- Counting

---

## Author

**Yasaswini Lakshmi**

Solved using **Python 🐍**