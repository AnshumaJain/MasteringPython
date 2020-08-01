def isPalindrome(x: int) -> bool:

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

print(isPalindrome())