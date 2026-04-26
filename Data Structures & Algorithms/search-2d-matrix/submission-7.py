class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0,ROW-1

        while top <= bot:
            req = (top+bot) >> 1
            if matrix[req][-1] < target:
                top = req+1
            elif matrix[req][0] > target:
                bot = req-1
            else:
                break
        
        if not (top <=bot):
            return False
        
        l,r = 0,COL-1

        while l<=r:
            m = (l+r) >> 1
            if matrix[req][m] == target:
                return True
            elif matrix[req][m] > target:
                r = m-1
            else:
                l = m+1
        return False