"""
LeetCode Problem #27: Remove Element

Given an array nums and a value val, remove all instances of that value in-place
and return the new length.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
"""
from typing import List


class Solution:

    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:

        if not nums:
            return len(nums)

        i = 0
        while 1:
            element = nums[i]
            if element == val:
                nums.remove(element)
                i -= 1

            i += 1
            if i > len(nums) - 1:
                break

        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    my_array = [3, 2, 2, 3]
    print(sol.remove_element(my_array, 3))
    print(my_array)
