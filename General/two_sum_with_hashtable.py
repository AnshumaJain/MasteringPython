"""
LeetCode Problem #1: Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""
from typing import List


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in hash_map:
                hash_map[num] = i
            else:
                return [hash_map[n], i]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.two_sum(nums, target))
