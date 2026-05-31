func permute(nums []int) [][]int {
    var res[][]int
    backTrack(&res, []int{}, nums, make([]bool, len(nums)))
    return res
}

func backTrack(res *[][]int, perm []int, nums []int, pick []bool){
    if len(perm) == len(nums){
        temp := append([]int{}, perm...)
        *res = append(*res, temp)
    }

    for i:=0; i <len(nums);i++{
        if !pick[i]{
            perm = append(perm, nums[i])
            pick[i] = true
            backTrack(res, perm, nums, pick)
            perm = perm[:len(perm)-1]
            pick[i] = false
        }
    }
}
