class Solution:
    def findMedianSortedArrays(self, nums1=[], nums2=[]) -> float:


        nums1.append(nums2)












        p = len(add)

        if p % 2 == 0:
            median = (nums1[p//2] + nums1[(p//2)-1])/2
        else:
            median = nums1[p//2]

        return add
        return median

p = Solution()
print(p.findMedianSortedArrays([2,3],[1,4]))