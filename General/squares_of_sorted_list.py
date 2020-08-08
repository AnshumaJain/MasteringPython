"""
LeetCode Problem #977: Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an
array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

Example 2:
Input: [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order
"""


def sorted_squares(A):
    if len(A) == 0:
        return A
    elif len(A) == 1:
        return [x ** 2 for x in A]

    pos = []
    neg = []
    merge = []
    for i in A:
        if i < 0:
            i *= -1
            neg.append(i)
        else:
            pos.append(i)

    neg = neg[::-1]
    if len(neg) == 0:
        return [x ** 2 for x in pos]
    elif len(pos) == 0:
        return [x ** 2 for x in neg]

    n = 0
    p = 0
    while 1:
        if neg[n] > pos[p]:
            merge.append(pos[p]**2)
            p += 1
            if p == len(pos):
                merge += (x ** 2 for x in neg[n:])
                break
        else:
            merge.append(neg[n]**2)
            n += 1
            if n == len(neg):
                merge += (x ** 2 for x in pos[p:])
                break
    return merge


if __name__ == "__main__":
    print(sorted_squares([-4, -1, 0, 3, 10]))
