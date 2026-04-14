class MinStack:

    def __init__(self):
        self.s1 = []
        self.minS = []

    def push(self, val: int) -> None:
        if self.minS:
            mv = self.minS[-1]
        else:
            mv = float("infinity")
        mv = min(mv, val)       
        self.s1.append(val)
        self.minS.append(mv)

    def pop(self) -> None:
        self.minS.pop()
        self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]      

    def getMin(self) -> int:
        return self.minS[-1]
