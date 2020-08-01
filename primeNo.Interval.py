
import math

start = int(input(' Enter the interval from ='))
end = int(input('to='))

List_prime = [2]             #list of prime no.s
length = len(List_prime)

for i in range(3, end):

    for j in range(0, length):

        Check_prime = i % List_prime[j]

        if Check_prime == 0:
            break

    if j == (length - 1) and Check_prime != 0:

        List_prime.append(i)
        length += 1

subset_list = []

for k in range(start, end):
    if k in List_prime : #learned new
        subset_list.append(k)

print subset_list
#print List_prime
#print list_prime.range (start,end)