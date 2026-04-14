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
        
        # # return (1+max(self.maxDepth(root.left),self.maxDepth(root.right))) dfs

        # stack = [[root,1]] iterative
        # res=0

        # while stack:
        #     node,v=stack.pop()

        #     if node:
        #         res = max(res,v)
        #         stack.append([node.left,v+1])
        #         stack.append([node.right,v+1])
        # return res
        q = deque() #bfs

        if root:
            q.append(root)
        level=0
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level
