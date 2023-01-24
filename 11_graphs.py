from typing import List, Optional
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        200. Number of Islands
        Iterate through each of the cell and if it is an island,
        do dfs to mark all adjacent islands,
        then increase the counter by 1
        """

        width, height = len(grid[0]), len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        number = 0

        def dfs(r, c):
            if not r in range(height) or not c in range(width) or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            # print(*grid)
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(height):
            for c in range(width):
                if grid[r][c] == "1":
                    dfs(r, c)
                    number += 1

        return number


if __name__ == "__main__":
    s = Solution()

grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

print(grid2)
print(s.numIslands(grid2))
