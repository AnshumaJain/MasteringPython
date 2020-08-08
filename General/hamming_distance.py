"""
LeetCode Problem #461: Hamming Distance

The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note: 0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4

Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""
from decimal_to_binary import *


def hamming_distance(x, y):

    x = decimal_to_binary(x)
    y = decimal_to_binary(y)

    hamming_dist = 0
    for i in range(0, len(x)):
        if x[i] != y[i]:
            hamming_dist += 1

    return hamming_dist


if __name__ == "__main__":
    # 0 ≤ x, y < 231
    print("A")
    print(hamming_distance(0, 4294967295))
    print("B")
