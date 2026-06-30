# LC-1732: Find the Highest Altitude

## Problem

There is a biker going on a road trip. The trip consists of `n + 1` points at different altitudes.

You are given an integer array `gain` where `gain[i]` is the net gain in altitude between points `i` and `i + 1`.

The biker starts at altitude **0**.

Return the **highest altitude** reached during the trip.

---

## Intuition

The altitude changes continuously as we move through the array.

Instead of storing every altitude, we can maintain:

* `current_altitude` → Current altitude after each gain.
* `highest_altitude` → Maximum altitude reached so far.

At every step:

1. Update the current altitude.
2. Compare it with the highest altitude.
3. Update the maximum if necessary.

This allows us to solve the problem in a single traversal.

---

## Approach

1. Initialize:

   * `current_altitude = 0`
   * `highest_altitude = 0`
2. Traverse the `gain` array.
3. Add each value to `current_altitude`.
4. Update `highest_altitude` if the current altitude is greater.
5. Return `highest_altitude`.

---

## Example

### Input

```python
gain = [-5,1,5,0,-7]
```

### Dry Run

|  Gain | Current Altitude | Highest Altitude |
| ----: | ---------------: | ---------------: |
| Start |                0 |                0 |
|    -5 |               -5 |                0 |
|    +1 |               -4 |                0 |
|    +5 |                1 |                1 |
|     0 |                1 |                1 |
|    -7 |               -6 |                1 |

### Output

```python
1
```

---

## Time Complexity

**O(N)**

The array is traversed exactly once.

---

## Space Complexity

**O(1)**

Only two integer variables are used.

---

## Pattern

* Arrays
* Prefix Sum
* Running Sum
* Simulation

---

## Key Takeaway

Instead of storing every altitude, maintain a **running sum** (current altitude) and continuously track the **maximum value** reached.

This is a classic **Prefix Sum / Running Sum** pattern and achieves **O(N)** time with **O(1)** extra space.
