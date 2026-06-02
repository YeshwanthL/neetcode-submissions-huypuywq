func makesquare(matchsticks []int) bool {
    totalLength := 0
    for _,m := range matchsticks{
        totalLength += m
    }
    if totalLength%4 !=0 {
        return false
    }
    length := totalLength/4
    sides := make([]int, 4)
    sort.Sort(sort.Reverse(sort.IntSlice(matchsticks)))

    var dfs func(index int) bool
    dfs = func(index int) bool {
        if index == len(matchsticks){
            return true
        }

        for i := 0; i<4; i++ {
            if sides[i]+matchsticks[index] <= length{
                sides[i] += matchsticks[index]
                if dfs(index+1){
                    return true
                }
                sides[i] -= matchsticks[index]
            }
            if sides[i] == 0{
                break
            }
        }
        return false
    }
    return dfs(0)
}
