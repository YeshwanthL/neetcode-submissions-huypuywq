# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, cur_max):
            if not root:
                return 0
            
            res = 1 if root.val >= cur_max else 0
            cur_max = max(cur_max, root.val)
            res += dfs(root.left, cur_max)
            res += dfs(root.right, cur_max)
            return res
        return dfs(root, root.val)

