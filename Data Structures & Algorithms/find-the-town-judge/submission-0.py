class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for inc, out in trust:
            delta[inc] -= 1
            delta[out] += 1
        
        for i in range(n+1):
            if delta[i] == n-1:
                return i
        return -1