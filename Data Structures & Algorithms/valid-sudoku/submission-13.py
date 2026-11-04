class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        SQUARES = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                cell = board[r][c]
                if cell == '.':
                    continue
                elif cell in ROWS[r] or cell in COLS[c] or cell in SQUARES[(r//3, c//3)]:
                    return False
                ROWS[r].add(cell)
                COLS[c].add(cell)
                SQUARES[(r//3, c//3)].add(cell)
        return True