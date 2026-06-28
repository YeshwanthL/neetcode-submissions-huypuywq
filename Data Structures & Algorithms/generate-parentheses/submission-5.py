class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(openB, closedB):
            if openB == closedB == n:
                res.append("".join(stack))
                return
            
            if openB < n:
                stack.append("(")
                dfs(openB+1, closedB)
                stack.pop()
            
            if closedB < openB:
                stack.append(")")
                dfs(openB, closedB+1)
                stack.pop()
        dfs(0, 0)
        return res