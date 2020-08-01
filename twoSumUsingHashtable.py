
class Solution:
    """
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
