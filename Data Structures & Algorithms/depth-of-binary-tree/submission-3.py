# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # if not root:
        #     return 0
        
        # return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))

        # q = deque() dfs/level order

        # if root:
        #     q.append(root)
        # level=0
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level+=1
        # return level

        if not root:
            return 0
        
        res=0
        stack= [[root,1]]
        cur = root

        while stack:
            node,v = stack.pop()
            if node:
                res = max(res,v)
                stack.append([node.left,1+v])
                stack.append([node.right,1+v])
        return res
