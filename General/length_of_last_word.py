"""
LeetCode Problem #58: Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop
from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""


class Solution:

    @staticmethod
    def length_of_last_word(s: str) -> int:

        if s == "":
            return 0
        count = 0
        temp = " "
        p = 0
        for i in s[::-1]:
            p += 1
            if i != " ":
                count += 1
            if i == " " and temp != " ":
                return count
            if p == len(s):
                return count
            temp = i


if __name__ == "__main__":
    sol = Solution()
    print(sol.length_of_last_word("i love eating burger"))
    print(sol.length_of_last_word("hello world"))
    print(sol.length_of_last_word("i use triple pillow"))
