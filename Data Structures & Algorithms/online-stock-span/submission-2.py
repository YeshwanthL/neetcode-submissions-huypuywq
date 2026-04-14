class StockSpanner:

    def __init__(self):
        self.tracker = []

    def next(self, price: int) -> int:
        res = 1
        while self.tracker and self.tracker[-1][0] <= price:
            res += self.tracker[-1][1]
            self.tracker.pop()
        self.tracker.append((price,res))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)