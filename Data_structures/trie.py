"""
LeetCode Problem #208: Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

class Trie:

    def __init__(self):
        """
        Initializes the data structure.
        """
        self.head = {}

    def insert(self, word: str) -> str:
        """
        Inserts a word into the trie.
        """
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True
        # print(self.head)
        return word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.head
        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True


if __name__ == "__main__":
    p = Trie()
    p.insert("hell")
    p.insert("hello")
    p.insert("flower")
    p.insert("flow")
    p.insert("flight")

    print(p.search("hello"))
    print(p.search("hell"))
    print(p.search("he"))
    print(p.search("helloi"))
    print(p.starts_with("hell"))
    print(p.starts_with("fle"))
    print(p.starts_with("\\"))
