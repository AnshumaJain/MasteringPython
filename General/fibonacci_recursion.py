# Print the fibonacci sum for a given number using recursion

def fibonacci_recursion(num):

    # Base case
    if num == 1:  # fib(1) = 1
        return 1
    elif num == 0:  # fib(0) = 0
        return 0

    return fibonacci_recursion(num-1) + fibonacci_recursion(num-2)


if __name__ == "__main__":

    n = int(input("Enter a positive integer number: "))
    print("Fibonacci sum for the given number: ", fibonacci_recursion(n))
