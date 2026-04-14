class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                tmp = ""
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*tmp)
        return "".join(stack)