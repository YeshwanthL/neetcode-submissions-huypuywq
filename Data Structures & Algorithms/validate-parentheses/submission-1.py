class Solution:
    def isValid(self, s: str) -> bool:
        Map  ={"]":"[","}":"{",")":"("}
        stack = []

        for p in s:
            if p not in Map :
                stack.append(p)
                continue
            if not stack or stack[-1] != Map[p]:
                return False
            stack.pop()
        return not stack