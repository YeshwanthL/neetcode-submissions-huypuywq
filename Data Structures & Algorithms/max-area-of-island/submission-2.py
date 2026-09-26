class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        path = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 0 or (r, c) in path:
                return 0
            path.add((r, c))
            return 1 + dfs(r, c+1) + dfs(r, c-1) + dfs(r+1, c) + dfs(r-1, c)
        
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    tmp = dfs(r, c)
                    res = max(res, tmp)
        return res