class Solution:
    def __init__(self):
        """
        Initialize your data structure here.
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
        print(self.head)
        return strs

    def longestCommonPrefix(self, strs) -> str:
        self.insert(strs)
        prefix = ""
        cur = self.head
        if strs == []:
            return prefix
        while 1:
            for ch in cur:
                if ch == '*' or len(cur) > 1:
                    return prefix
                else:
                    prefix = prefix + ch

            cur = cur[ch]

        return prefix


p = Solution()

print(p.longestCommonPrefix([]))