"""""
Given an array of integers nums, sort the array in ascending order using Shell sort.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
"""""
from typing import List


def shell_sort(nums: List[int]) -> List[int]:

    ln = len(nums)

    if ln == 1 or ln == 0:
        return nums

    if ln == 2:
        if nums[0] < nums[1]:
            return nums
        else:
            nums.reverse()
            return nums

    for j in range(1, ln - 1):
        n = ln // (2 ** j)

        for i in range(0, ln):
            if (i + n) < ln and nums[i] >= nums[i + n]:
                nums[i], nums[i + n] = nums[i + n], nums[i]

                my_indices = list(range(0, i + 1))
                my_indices.reverse()
                for k in my_indices:
                    if nums[k] <= nums[k - n] and k >= n:
                        nums[k - n], nums[k] = nums[k], nums[k - n]

    return nums


if __name__ == "__main__":

    test_array = [
        [15, 2, 5, 6, 3],
        [1, 2, 5, 6, 4, 3],
        [10, 10, 1, 1],
        [10, 5, 20],
        [1, 2, 3, 4, 100, 5, 200],
        [10, 20, 10, 20],
        [1, -2, 1, 2],
        [2, 1],
        [-7087, 12694, -19352, -7660, 12052, -11316, -352]
    ]
    for unsorted_list in test_array:
        op = shell_sort(unsorted_list)
        print(op)
