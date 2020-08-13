"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

"""
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        priority_queue = deque()
        total_rows = 0
        count_fresh = 0
        for i, row in enumerate(grid):  # counting the given rotten and fresh oranges
            total_rows += 1
            total_cols = 0
            for j, col in enumerate(row):
                total_cols += 1
                if col == 2:
                    priority_queue.append([i, j])
                if col == 1:
                    count_fresh += 1

        if count_fresh == 0:  # if all given oranges are rotten return 0
            return 0

        time_count = 0
        loop_count = 0
        break_point = len(priority_queue)

        while priority_queue:  # BFS for rotten oranges rotting fresh oranges

            if loop_count == break_point:
                break_point += len(priority_queue)
                time_count += 1  # Incrementing count with the branching out levels
            loop_count += 1
            [x, y] = priority_queue.popleft()

            if 0 <= x - 1:
                if grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    priority_queue.append([x - 1, y])

            if x + 1 < total_rows:
                if grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    priority_queue.append([x + 1, y])

            if 0 <= y - 1:
                if grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    priority_queue.append([x, y - 1])

            if y + 1 < total_cols:
                if grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    priority_queue.append([x, y + 1])

        for row in grid:  # if any fresh orange is left return -1
            for col in row:
                if col == 1:
                    return -1

        return time_count  # if everything got rot by the end return the time it took

