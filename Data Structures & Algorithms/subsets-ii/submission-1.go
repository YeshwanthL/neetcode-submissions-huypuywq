func subsetsWithDup(nums []int) [][]int {
    var res [][]int
    sort.Ints(nums)

    var dfs func (int, []int)
    dfs = func(i int, subset []int){
        if i == len(nums){
            res = append(res, append([]int{}, subset...))
            return
        }
        subset = append(subset, nums[i])
        dfs(i+1, subset)
        subset = subset[:len(subset)-1]

        for i+1 < len(nums) && nums[i] == nums[i+1]{
            i++
        }
        dfs(i+1, subset)
    }
    dfs(0, []int{})
    return res
}
