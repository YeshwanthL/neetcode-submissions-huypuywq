class Solution:
    def isValid(self, s: str) -> bool:
        store = { '}' : '{', ']' : '[', ')' : '('}
        stack = []

        for c in s:
            if stack and c in store and stack[-1] == store[c]:
                stack.pop()
                continue
            stack.append(c)
        return False if stack else True