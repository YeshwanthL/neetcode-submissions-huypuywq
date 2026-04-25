class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []

        for o in operations:
            if  o == '+':
                a,b = stack[-1], stack[-2]
                stack.append(a+b)
                res += a+b
            elif o == 'D':
                a = stack[-1]
                stack.append(a*2)
                res += a*2
            elif o == 'C':
                a = stack.pop()
                res -= a
            else:
                res += int(o)
                stack.append(int(o))
        return res 