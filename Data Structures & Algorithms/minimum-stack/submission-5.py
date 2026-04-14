class MinStack:

    def __init__(self):
        self.s1 = []
        self.minS = []

    def push(self, val: int) -> None:  
        self.s1.append(val)
        val = min(val, self.minS[-1] if self.minS else val)  
        self.minS.append(val)

    def pop(self) -> None:
        self.minS.pop()
        self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]      

    def getMin(self) -> int:
        return self.minS[-1]
