class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1 or n == 1:
            return 1
        elif m == 2 and n == 2:
            return 2

        path = 0
        n -= 1
        for i in range(0, m):

            path = self.uniquePaths(m - i, n) + path

        return path0=-23qweXZ

p = Solution()
print(p.uniquePaths(7, 3))