
num = int(input("enter the number="))

def factorial(n):
    return 1 if n == 1 or 0 else n * factorial(n - 1)

print('factorial of', num, 'is =', factorial(num))


def Largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [94, 6, 87, 57]
n = len(arr)
ans = Largest(arr, n)
#print("the largest array in the given list is", ans)

10 + 20
#print("for")

