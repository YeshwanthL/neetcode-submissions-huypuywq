class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, j = stack.pop()
                diff = i - j
                res[j] = diff
            stack.append([t,i])
        return res
        