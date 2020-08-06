"""
LeetCode Problem #14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""


class Solution:
    def __init__(self):
        """
        Initializes the data structure.
        """
        self.head = {}

    def insert(self, strs):
        """
        Inserts a word into the trie.
        """
        for word in strs:
            cur = self.head
            for ch in word:
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
            cur['*'] = True
        # print(self.head)
        return strs

    def longest_common_prefix(self, strs) -> str:
        self.insert(strs)
        prefix = ""
        cur = self.head
        if not strs:
            return prefix
        while 1:
            for ch in cur:
                if ch == '*' or len(cur) > 1:
                    return prefix
                else:
                    prefix = prefix + ch
            cur = cur[ch]
        return prefix


if __name__ == "__main__":
    p = Solution()
    print("Longest prefix:", p.longest_common_prefix(["flower", "flow", "flight"]))
    print("Longest prefix:", p.longest_common_prefix(["dog", "racecar", "car"]))
