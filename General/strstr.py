"""
LeetCode Problem #28. Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf()
"""


class Solution:

    @staticmethod
    def strstr(haystack: str, needle: str) -> int:

        if needle == "" or haystack == needle:
            return 0

        if needle in haystack:
            for i in range(0, len(haystack) - 1):
                if haystack[i:len(needle) + i] == needle:
                    return i

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strstr("Hello", "ll"))
    print(sol.strstr("aaaaa", "bba"))
