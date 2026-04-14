class StockSpanner:

    def __init__(self):
        self.tracker = []

    def next(self, price: int) -> int:
        res = 1
        for i in range(len(self.tracker)-1, -1, -1):
            if price >= self.tracker[i]:
                res += 1
            else:
                break
        self.tracker.append(price)
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)