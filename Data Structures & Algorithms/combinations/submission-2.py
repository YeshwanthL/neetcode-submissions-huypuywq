class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if i > n:
                if len(curr) == k:
                    res.append(curr.copy())
                return
            curr.append(i)
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        dfs(1, [])
        return res