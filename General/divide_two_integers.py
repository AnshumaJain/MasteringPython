"""
LeetCode Problem #29: Divide Two Integers

Given two integers dividend and divisor, divide two integers
without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part.
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
"""


def divide(dividend: int, divisor: int) -> int:
    count = 0
    i = 0
    is_neg = 0
    if dividend < 0:
        dividend *= -1
        is_neg += 1
    if divisor < 0:
        divisor *= -1
        is_neg += 1

    if divisor == 1:
        count = dividend
        if count < -(2 ** 31) or count > (2 ** 31) - 1:
            count = (2 ** 31) - 1
        if is_neg == 1:
            count = dividend * (-1)
        return count

    while 1:
        i += divisor
        count += 1
        if i == dividend:
            if is_neg == 1:
                count *= -1
            return count
        elif i > dividend:
            count -= 1
            if is_neg == 1:
                count *= -1
            return count

    if count < -(2 ** 31) or count > (2 ** 31) - 1:  # is this code even executed?
        count = (2 ** 31) - 1
        if is_neg == 1:
            count *= -1
        return count


if __name__ == "__main__":
    print(divide(-100.7, 2))
    print(divide(2147483647, 2))  # time limit exceeds for this test case
