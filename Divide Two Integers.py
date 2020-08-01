
"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
"""


def divide(dividend: int, divisor: int) -> int:
    count = 0
    i = 0
    val = 0
    p = 0
    if dividend < 0:
        dividend *= -1
        p += 1
    if divisor < 0:
        divisor *= -1
        p += 1

    if divisor == 1:
        count = dividend
        if count < -(2 ** 31) or count > (2 ** 31) - 1:
            count = (2 ** 31) - 1
        if p == 1:
            count = dividend * (-1)
        return count

    while 1:
        i += divisor
        count += 1
        if i == dividend:
            if p == 1:
                count *= -1
            return count

        elif i > dividend:
            count -= 1
            if p == 1:
                count *= -1
            return count

    if count < -(2 ** 31) or count > (2 ** 31) - 1:
        count = (2 ** 31) - 1
        if p == 1:
            count *= -1
        return count


print(divide(-2147483648, 2))