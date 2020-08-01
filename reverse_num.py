def reverse(x: int) -> int:
    rev = 0
    while x != 0:
        pop = x % 10
        x //= 10

        temp = rev * 10 + pop
        rev = temp

    return rev

print(reverse(-123))