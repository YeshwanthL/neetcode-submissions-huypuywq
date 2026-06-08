func solveNQueens(n int) [][]string {
	res := [][]string{}
    board := make([][]string, n)
    for i:= range board{
        board[i] = make([]string, n)
        for j := range board[i]{
            board[i][j] = "."
        }
    }

    var backtrack func(r int)
    backtrack = func(r int){
        if r == n {
            copyBoard := make([] string, n)
            for i := range board{
                copyBoard[i] = ""
                for j := range board[i]{
                    copyBoard[i] += board[i][j]
                }
            }
            res = append(res, copyBoard)
            return
        }
        for c:=0; c<n;c++{
            if isSafe(r, c, board){
                board[r][c] = "Q"
                backtrack(r+1)
                board[r][c] = "."
            }
        }
    }
    backtrack(0)
    return res
}

func isSafe(r,c int, board[][]string) bool{
    for row:=r-1; row>=0; row--{
        if board[row][c] == "Q"{
            return false
        }
    }

    for row,col:=r-1,c-1; row >= 0 && col>=0; row,col=row-1, col-1{
        if board[row][col] == "Q"{
            return false
        }
    }

    for row, col:= r-1,c+1; row >=0 && col < len(board); row,col = row-1,col+1{
        if board[row][col] == "Q"{
            return false
        }
    }
    return true
}