import numpy as np
import math

def heap_sort(input_list):


# MAX HEAP:-
    my_indices = range(1, len(input_list))
    my_indices.reverse()

    for i in my_indices:
        if i % 2 == 0:
            if input_list[i] > input_list[(i/2)-1]:
                swap(input_list, (i/2)-1, i)
        else:
            if input_list[i] > input_list[i / 2]:
                swap(input_list, i / 2, i)

# HEAPIFY + SORT :-
    for j in range(0, len(input_list)-1):
        swap(input_list, 0, len(input_list)-1-j)

        p = 0
        level = int(np.log2(len(input_list)-1-j))
        k = 0
        while k < level:

                if (2*p) + 2 == len(input_list)-1-j:
                    if input_list[(2*p) + 1] > input_list[p]:
                        swap(input_list, p, (2*p) + 1)
                        p = (2 * p) + 1

                elif input_list[(2*p) + 1] > input_list[(2*p) +2]:
                    if input_list[(2*p) + 1] > input_list[p]:
                        swap(input_list, p, (2 * p) + 1)
                        p = (2 * p) + 1
                else:
                    if input_list[(2 * p) + 2] > input_list[p]:
                        swap(input_list, p, (2 * p) + 2)
                        p = (2 * p) + 2
                k+=1

    return input_list

def swap(list , n, m):
    temp = list[m]
    list[m] = list[n]
    list[n] = temp


test_array = [
    [15, 2, 5, 6, 3],
    [1, 2, 5, 6, 4, 3],
    [10, 10, 1, 1],
    [10, 5, 20],
    [1, 2, 3, 4, 100, 5, 200],
    [10, 20, 10, 20],
    [1, 2, 1, 2],
]

for l in test_array:
    op = heap_sort(l)
    print op

 # Knowledge: import heapq
 #   heapq.heapify(list)
 #   heapq.heappush(list)- for adding no. at the end
 #   heapq.heappop(list)- for getting the root of the list tree