# Pascal's Triangle

## Problem

Given an integer `numRows`, return the first `numRows` of Pascal's Triangle.

In Pascal's Triangle:

* The first and last element of every row is `1`.
* Every other element is the sum of the two elements directly above it.

## Approach

1. Create an empty list called `triangle`.
2. Iterate from `0` to `numRows - 1`.
3. For each row:

   * Initialize a list filled with `1`s of length `i + 1`.
   * Update the middle elements using the previous row:

     * `row[j] = triangle[i-1][j-1] + triangle[i-1][j]`
4. Append the completed row to the triangle.
5. Return the completed triangle.

## Time Complexity

* **O(numRows²)**

Each row is processed once, and the inner loop computes the middle elements.

## Space Complexity

* **O(numRows²)**

The entire Pascal's Triangle is stored and returned.
