"""""
Given an array of integers nums, sort the array in ascending order using Selection sort.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
"""""
from typing import List


def selection_sort(input_list: List[int])  -> List[int]:

    for j in range(0, len(input_list)):
        [min, min_index] = [input_list[j], j]
        for i in range(j, len(input_list)):
            if input_list[i] < min:
                min = input_list[i]
                min_index = i

        temp = input_list[j]
        input_list[j] = min
        input_list[min_index] = temp

    return input_list


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
        op = selection_sort(unsorted_list)
        print(op)

