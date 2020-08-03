"""
LeetCode Problem # 46: Permutations
Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:

    n = len(nums)
    if n == 0:
        return [nums]
    elif n == 1:
        return [nums]
    elif n == 2:
        return [nums, nums[::-1]]

    my_nums = []
    for i in range(0, n):
        for j in permute(nums[0:i] + nums[(i+1):n]):
            my_nums.append([nums[i]] + j)

    return my_nums


if __name__ == "__main__":
    a = permute([1, 2, 3, 4])

    for i in a:
        print(i)