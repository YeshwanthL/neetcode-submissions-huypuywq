/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 
func rob(root *TreeNode) int {
    result := dfs(root)
    return max(result[0], result[1])
}

func dfs(root * TreeNode) [2]int {
    if root == nil{
        return [2]int{0, 0}
    }

    left := dfs(root.Left)
    right := dfs(root.Right)

    withRoot := root.Val + left[1] + right[1]
    withoutRoot := max(left[0], left[1]) + max(right[0], right[1])

    return [2]int{withRoot, withoutRoot} 
}

func max(a, b int) int{
    if a > b{
        return a
    }
    return b
}