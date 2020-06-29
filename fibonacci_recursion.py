
def fibonacci_recursion(n):

    # Base case
    if n == 1:  # Fib(1) = 1
        return 1
    elif n == 0:  # Fib(0) = 0
        return 0

    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


if __name__ == "__main__":

    n = int(input("Enter a positive integer number : "))
    print("Fibonacci sum for the given number : ", fibonacci_recursion(n))



