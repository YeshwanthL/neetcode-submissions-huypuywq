class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def addCell(r, c):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == -1:
                return
            q.append([r,c])
            visit.add((r,c))
        
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                visit.add((r,c))
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c-1)
                addCell(r,c+1)
            dist += 1