func permuteUnique(nums []int) [][]int {
    res := make(map[string][]int)
    perm := []int{}

    var dfs func()
    dfs = func(){
        if len(perm) == len(nums){
            temp := make([]int, len(perm))
            copy(temp, perm)
            key := fmt.Sprint(temp)
            res[key] = temp
            return
        }

        for i:=0; i<len(nums); i++{
            if nums[i] != -1001{
                temp := nums[i]
                perm = append(perm, nums[i])
                nums[i] = -1001
                dfs()
                nums[i] = temp
                perm = perm[:len(perm)-1]
            }
        }
    }
    dfs()
    result := [][]int{}
    for _,v := range res{
        result = append(result,v)
    }
    return result
}
