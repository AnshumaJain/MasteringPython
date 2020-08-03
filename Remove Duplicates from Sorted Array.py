"""
Given a sorted array nums, remove the duplicates in-place such that each
element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums
being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums
being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification
to the input array will be known to the caller as well.
"""


def remove_duplicates(nums) -> int:
    if not nums:
        return len(nums)

    temp = None
    count = 1
    i = 0
    while 1:
        val = nums[i]
        if val == temp:
            count += 1

        temp = val

        if count > 1:
            nums.remove(val)
            i -= 1
            count -= 1

        i += 1
        if i > len(nums) - 1:
            break

    return len(nums)


if __name__ == "__main__":

    input_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicates(input_list))
    print(input_list)
