"""
LeetCode Problem #7: Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""


def reverse(num: int) -> int:

    negative = False
    if num < 0:
        negative = True
        num *= -1

    rev = 0
    while num:
        pop = num % 10
        num //= 10
        rev = rev * 10 + pop

    if negative:
        rev *= -1

    if rev > (2**31) - 1 or rev < -2**31:
        return 0

    return rev


if __name__ == "__main__":
    print(reverse(-123))
    print(reverse(123))
    print(reverse(120))
