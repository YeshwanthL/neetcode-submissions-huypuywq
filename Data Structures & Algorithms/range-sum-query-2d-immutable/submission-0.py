class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.pre_sum = [ [0]*(cols+1) for _ in range(rows+1) ]

        for r in range(rows):
            cur = 0
            for c in range(cols):
                cur += matrix[r][c]
                above = self.pre_sum[r][c+1]
                self.pre_sum[r+1][c+1] = cur + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1+1
        r2 = row2+1
        c1 = col1+1
        c2 = col2+1

        bottom = self.pre_sum[r2][c2]
        top_right = self.pre_sum[r1-1][c2]
        left = self.pre_sum[r2][c1-1]
        top_left = self.pre_sum[r1-1][c1-1]

        return bottom-top_right-left+top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)