"""
LeetCode Problem #35: Search Insert Position

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""
from typing import List


class Solution:

    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:

        for i in range(0, len(nums)):
            if target < nums[0]:
                return 0
            elif target > nums[len(nums) - 1]:
                return len(nums)
            elif nums[i] == target:
                return i
            elif i != len(nums) - 1:
                if nums[i] < target < nums[i + 1]:
                    return i + 1


if __name__ == "__main__":

    sol = Solution()
    print(sol.search_insert([1, 3, 5, 6], 5))
    print(sol.search_insert([1,3,5,6], 2))
    print(sol.search_insert([1, 3, 5, 6], 7))
    print(sol.search_insert([1, 3, 5, 6], 0))
