"""""
Given an array of integers nums, sort the array in ascending order using Heap sort.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
"""""
from typing import List
import numpy as np


def heap_sort(input_list: List[int]) -> List[int]:
    # MAX HEAP
    my_indices = list(range(1, len(input_list)))
    my_indices.reverse()

    for i in my_indices:
        if i % 2 == 0:
            if input_list[i] > input_list[(i // 2) - 1]:
                swap(input_list, (i // 2) - 1, i)
        else:
            if input_list[i] > input_list[i // 2]:
                swap(input_list, i // 2, i)

    # HEAPIFY + SORT
    for j in range(0, len(input_list) - 1):
        swap(input_list, 0, len(input_list) - 1 - j)

        p = 0
        level = int(np.log2(len(input_list) - 1 - j))
        k = 0
        while k < level:
            if (2 * p) + 2 == len(input_list) - 1 - j:
                if input_list[(2 * p) + 1] > input_list[p]:
                    swap(input_list, p, (2 * p) + 1)
                    p = (2 * p) + 1

            elif input_list[(2 * p) + 1] > input_list[(2 * p) + 2]:
                if input_list[(2 * p) + 1] > input_list[p]:
                    swap(input_list, p, (2 * p) + 1)
                    p = (2 * p) + 1
            else:
                if input_list[(2 * p) + 2] > input_list[p]:
                    swap(input_list, p, (2 * p) + 2)
                    p = (2 * p) + 2
            k += 1

    return input_list


def swap(input_list, n, m):
    temp = input_list[m]
    input_list[m] = input_list[n]
    input_list[n] = temp


if __name__ == "__main__":

    test_array = [
        [15, 2, 5, 6, 3],
        [1, 2, 5, 6, 4, 3],
        [10, 10, 1, 1],
        [10, 5, 20],
        [1, 2, 3, 4, 100, 5, 200],
        [10, 20, 10, 20],
        [1, -2, 1, 2],
    ]

    for unsorted_list in test_array:
        op = heap_sort(unsorted_list)
        print(op)

# Knowledge: import heapq
#   heapq.heapify(list)
#   heapq.heappush(list)- for adding no. at the end
#   heapq.heappop(list)- for getting the root of the list tree
