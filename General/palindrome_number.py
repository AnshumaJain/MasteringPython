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
