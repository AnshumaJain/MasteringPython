"""""
Given an array of integers nums, sort the array in ascending order using shell sort.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
"""""
from typing import List


class Solution:

    @staticmethod
    def sort_array(nums: List[int]) -> List[int]:

        ln = len(nums)

        for j in range(1, ln - 1):
            n = (ln // (2 ** j))

            for i in range(0, ln):

                if (i + n) < ln and nums[i] >= nums[i + n]:
                    nums[i], nums[i + n] = nums[i + n], nums[i]

                    my_indices = list(range(0, i + 1))
                    my_indices.reverse()
                    for k in my_indices:
                        if nums[k] <= nums[k - n] and k >= n:
                            nums[k - n], nums[k] = nums[k], nums[k - n]

        return nums

test_array = [
            [15, 2, 5, 6, 3],
            [1, 2, 5, 6, 4, 3],
            [10, 10, 1, 1],
            [10, 5, 20],
            [1, 2, 3, 4, 100, 5, 200],
            [10, 20, 10, 20],
            [1, -2, 1, 2],
        ]

obj = Solution()
for l in test_array:
    op = obj.sort_array(l)
    print(op)

