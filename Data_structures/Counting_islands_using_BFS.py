"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""


import
from collections import deque


class Solution:

    def __init__(self):  # initialise attributes of the class

        self.num_of_islands = 0
        self.priority_queue = deque()
        self.no_more_islands = False

    def numIslands(self, grid) -> int:  # returns total num of islands

        self.grid = grid
        if self.grid == []:
            return 0
        self.total_rows = len(self.grid)
        self.total_cols = len(self.grid[0])

        while 1:
            self.get_cordinates()

            if self.no_more_islands:
                return self.num_of_islands

            self.num_of_islands += self.count_islands()

    def get_cordinates(self):  # returns coordinates of value "1"

        for i, row in enumerate(self.grid):  # counting the islands
            for j, col in enumerate(row):
                last_val = col
                if col == "1":
                    self.priority_queue.append([i, j])
                    return

        if last_val == "0":
            self.no_more_islands = True

    def count_islands(self):  # finds one island at a time and returns it as +1

        while 1:  # BFS for marking Islands
            if not self.priority_queue:
                return 1
            [x, y] = self.priority_queue.popleft()
            self.grid[x][y] = "0"

            if x - 1 >= 0:
                if self.grid[x - 1][y] == "1":
                    self.grid[x - 1][y] = "0"
                    self.priority_queue.append([x - 1, y])

            if x + 1 < self.total_rows:
                if self.grid[x + 1][y] == "1":
                    self.grid[x + 1][y] = "0"
                    self.priority_queue.append([x + 1, y])

            if y - 1 >= 0:
                if self.grid[x][y - 1] == "1":
                    self.grid[x][y - 1] = "0"
                    self.priority_queue.append([x, y - 1])

            if y + 1 < self.total_cols:
                if self.grid[x][y + 1] == "1":
                    self.grid[x][y + 1] = "0"
                    self.priority_queue.append([x, y + 1])