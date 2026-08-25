class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 1
            if (i,j) in path:
                return 0
            path.add((i,j))
            peri = dfs(i, j+1) + dfs(i, j-1) + dfs(i+1, j) + dfs(i-1, j)
            return peri
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r, c)