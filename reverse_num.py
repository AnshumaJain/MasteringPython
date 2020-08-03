
def reverse(x: int) -> int:

    sign = 1
    if x < 0:
        x = x*-1
        sign = -1

    rev = 0
    while x != 0:
        pop = x % 10
        x //= 10
        print(x)
        temp = rev * 10 + pop
        rev = temp

    return sign*rev

print(reverse(-123))