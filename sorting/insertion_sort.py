"""""
Given an array of integers nums, sort the array in ascending order using Insertion sort.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
"""""
from typing import List


def insertion_sort(input_list: List[int]) -> List[int]:

    for i in range(0, len(input_list) - 1):
        if input_list[i+1] < input_list[i]:
            temp = input_list[i]
            input_list[i] = input_list[i+1]
            input_list[i + 1] = temp

            my_indices = list(range(0, i))
            my_indices.reverse()
            for j in my_indices:
                if input_list[j+1] < input_list[j]:
                    temp = input_list[j]
                    input_list[j] = input_list[j+1]
                    input_list[j+1] = temp

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
        op = insertion_sort(unsorted_list)
        print(op)
