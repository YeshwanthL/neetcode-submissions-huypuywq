class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                word = ""
                while stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * word)
                continue
            stack.append(c)
        return "".join(stack)