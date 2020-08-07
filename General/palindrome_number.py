"""
LeetCode Problem #9: Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
# Find out if the given integer is a palindrome


def is_palindrome(x: int) -> bool:

    if x < 0:
        return False

    num = x
    rev = 0
    while x != 0:
        pop = x % 10
        x //= 10

        temp = rev * 10 + pop
        rev = temp

    if num == rev:
        return True
    else:
        return False


if __name__ == "__main__":

    input = eval(input("Enter the string = "))
    print(is_palindrome(input))
