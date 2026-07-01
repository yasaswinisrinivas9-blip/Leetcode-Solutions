# LC-121: Best Time to Buy and Sell Stock

## Problem

You are given an array `prices` where `prices[i]` is the price of a stock on the `iᵗʰ` day.

Choose a single day to buy one stock and a different future day to sell it.

Return the **maximum profit** you can achieve. If no profit is possible, return `0`.

---

## Intuition

To maximize profit, we should always buy at the **lowest price seen so far** and sell at the **current day's price**.

While traversing the array:

* Keep track of the **minimum buying price** encountered.
* Calculate the profit if the stock is sold on the current day.
* Update the maximum profit whenever a larger profit is found.

This avoids checking every possible pair of days.

---

## Approach

1. Initialize:

   * `minimum_price = prices[0]`
   * `maximum_profit = 0`
2. Traverse the array from the second day.
3. Update the minimum price if a lower price is found.
4. Otherwise, calculate:

```python id="xg2vmu"
profit = current_price - minimum_price
```

5. Update the maximum profit if the current profit is larger.
6. Return the maximum profit.

---

## Example

### Input

```python id="ojh2tf"
prices = [7,1,5,3,6,4]
```

### Dry Run

| Day | Price | Minimum Price | Profit | Maximum Profit |
| --: | ----: | ------------: | -----: | -------------: |
|   1 |     7 |             7 |      0 |              0 |
|   2 |     1 |             1 |      0 |              0 |
|   3 |     5 |             1 |      4 |              4 |
|   4 |     3 |             1 |      2 |              4 |
|   5 |     6 |             1 |      5 |              5 |
|   6 |     4 |             1 |      3 |              5 |

### Output

```python id="pq2d0n"
5
```

Buy on day **2** (price = 1) and sell on day **5** (price = 6).

---

## Time Complexity

**O(N)**

The prices array is traversed exactly once.

---

## Space Complexity

**O(1)**

Only two variables are maintained throughout the traversal.

---

## Pattern

* Arrays
* Greedy
* Prefix Minimum
* Single Pass

---

## Key Takeaway

Instead of comparing every pair of buying and selling days, continuously maintain the **lowest price encountered so far**.

For each day, compute the profit if you sold on that day and update the maximum profit.

This greedy strategy solves the problem in **O(N)** time using **O(1)** extra space.
