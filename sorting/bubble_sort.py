"""""
Given an array of integers nums, sort the array in ascending order using Bubble sort.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
"""""
from typing import List


class Solution:
    @staticmethod
    def sort_array(self, nums: List[int]) -> List[int]:

        ln = len(nums)
        for j in range(0, ln):
            for i in range(0, (ln - 1)):
                if nums[i] > nums[i + 1] and i + 1 != ln:
                    # swap adjacent elements
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums
