# Reverse the digits in the given input integer

def reverse_num(num: int) -> int:

    sign = 1
    if num < 0:
        num = num*-1
        sign = -1

    rev = 0
    while num != 0:
        pop = num % 10
        num //= 10
        temp = rev * 10 + pop
        rev = temp

    return sign*rev


if __name__ == "__main__":

    print(reverse_num(-123))
