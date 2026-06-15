/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 
func preorderTraversal(root *TreeNode) []int {
    res := []int{}
    stack := []*TreeNode{}
    curr := root

    for curr != nil || len(stack) > 0{
        if curr != nil{
            res = append(res, curr.Val)
            stack = append(stack, curr.Right)
            curr = curr.Left
        } else{
            curr = stack[len(stack)-1]
            stack = stack[:len(stack)-1]
        }
    }
    return res
}
