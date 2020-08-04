# List all prime numbers between the specified start and end intervals
import math

start = int(input(' Enter the interval from: '))
end = int(input('to: '))

list_prime = [2]  # list of prime numbers
length = len(list_prime)
check_prime = None

for i in range(3, end):
    for j in range(0, length):
        check_prime = i % list_prime[j]
        if check_prime == 0:
            break

    if j == (length - 1) and check_prime != 0:
        list_prime.append(i)
        length += 1

subset_list = []

for k in range(start, end):
    if k in list_prime:
        subset_list.append(k)

print(subset_list)
#print List_prime
#print list_prime.range (start,end)