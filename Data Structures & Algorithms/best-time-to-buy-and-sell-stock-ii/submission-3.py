class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur = prices[0]
        for n in prices:
            if n > cur:
                res += (n-cur)
                cur = n
            if n <= cur:
                cur = n
        return res