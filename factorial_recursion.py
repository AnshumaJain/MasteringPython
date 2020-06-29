
def factorial_recursion(num):

    if num != 1:
        return num * factorial_recursion(num-1)
    else:  # Base case
        return 1  # 1! = 1


if __name__ == "__main__":

    n = int(input("Enter a positive integer number : "))
    print("Factorial of", n, ":", factorial_recursion(n))