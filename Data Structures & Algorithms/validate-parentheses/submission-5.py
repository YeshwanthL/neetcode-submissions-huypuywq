class Solution:
    def isValid(self, s: str) -> bool:
        store ={ '}' : '{', ')' : '(', ']' : '[' }
        stack = []
        for c in s:
            if stack:
                if c in store and store[c] == stack[-1]:
                    stack.pop()
                    continue
            stack.append(c)
        return False if stack else True