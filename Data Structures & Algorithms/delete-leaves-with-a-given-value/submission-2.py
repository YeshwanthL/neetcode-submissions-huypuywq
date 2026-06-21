# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        visit = set()
        parent = {root: None}

        while stack:
            cur = stack.pop()
            if not cur.left and not cur.right:
                if cur.val == target:
                    p = parent[cur]
                    if not p:
                        return None
                    if p.left == cur:
                        p.left = None
                    if p.right == cur:
                        p.right = None
            elif cur not in visit:
                stack.append(cur)
                visit.add(cur)
                if cur.left:
                    stack.append(cur.left)
                    parent[cur.left] = cur
                if cur.right:
                    stack.append(cur.right)
                    parent[cur.right] = cur
        return root