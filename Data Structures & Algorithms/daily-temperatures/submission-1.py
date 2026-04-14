class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for d,t in enumerate(temperatures):
            while stack and stack[-1][0] <t:
                temp,day =stack.pop()
                res[day]=d-day
            stack.append((t,d))
        return res