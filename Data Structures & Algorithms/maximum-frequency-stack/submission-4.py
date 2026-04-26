class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.freqStack = defaultdict(list)
        self.maxf = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.maxf = max(self.maxf, self.count[val])
        self.freqStack[self.count[val]].append(val)
        
    def pop(self) -> int:
        res = self.freqStack[self.maxf].pop()
        self.count[res] -= 1
        if not self.freqStack[self.maxf]:
            self.maxf -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()