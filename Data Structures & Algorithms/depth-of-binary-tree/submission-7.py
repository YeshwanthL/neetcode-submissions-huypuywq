# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root: rec
        #     return 0
        
        # return (1+ max(self.maxDepth(root.left),self.maxDepth(root.right)))

        # stack = [[root,1]] itr
        # res=0

        # while stack:
        #     node,dep = stack.pop()
        #     if node:
        #         res = max(res,dep)
        #         stack.append([node.left,dep+1])
        #         stack.append([node.right,dep+1])
        # return res

        q= deque()
        lvl=0
        if root:
            q.append(root)
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl+=1
        return lvl