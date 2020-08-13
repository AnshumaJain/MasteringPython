# def strStr(haystack: str, needle: str) -> int:
#     if needle == "":
#         return 0
#
#     if haystack == needle:
#         return 0
#
#     if needle in haystack:
#         for i in range(0, len(haystack) - 1):
#             if haystack[i:len(needle)+i] == needle:
#                 return i
#
#     return -1

# def searchinsert(nums, target: int) -> int:
#
#     for i in range(0, len(nums)):
#             if target <= nums[0]:
#                 return 0
#             elif target > nums[len(nums) - 1]:
#                 return (len(nums))
#             elif nums[i] == target:
#                 return i
#             elif i != len(nums) - 1 :
#                 if nums[i] < target and nums[i+1] > target:
#                     return(i+1)
#
#
# print(searchinsert([1,3,5,6], 6))


def lengthOfLastWord(s: str) -> int:
    if s == "":
        return 0
    count = 0
    temp = " "
    p = 0
    for i in s[::-1]:
        p += 1
        if i != " ":
            print("im here1")
            count += 1
        if i == " " and temp != " ":
            print("im here2")
            return count
        if p == len(s):
            print("im here3")
            return count
        temp = i


print(lengthOfLastWord("  "))


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            version_status = isBadVersion(1)
            if version_status:
                return 1
        elif n == 2:
            version_status = isBadVersion(1)
            if version_status:
                return 1
            else:
                version_status = isBadVersion(2)
                if version_status:
                    return 2
        elif isBadVersion(n) == False:
            return None

        start = 1
        end = n
        bad_version = False

        while 1:
            version = start + (end - start) // 2
            version_status = isBadVersion(version)
            print("version =", version)

            if version_status == False:
                print("in False ")
                start = version + 1
                bad_version = True

            elif version_status == True:
                print("in true")
                end = version - 1
                if bad_version == True or version == start:
                    print("in true bv")
                    return version
