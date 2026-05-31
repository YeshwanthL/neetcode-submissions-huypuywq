func combine(n int, k int) [][]int {
    res := [][]int{}

    var dfs func(i int, cur []int)
    dfs = func(i int, cur []int){
        if i > n{
            if len(cur) == k{
                temp := make([]int, len(cur))
                copy(temp, cur)
                res = append(res, temp)
            }
            return
        }
        cur = append(cur, i)
        dfs(i+1, cur)
        cur = cur[:len(cur)-1]
        dfs(i+1, cur)
    }
    dfs(1, []int{})
    return res
}
