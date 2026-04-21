class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        cur = prices[l]
        for r in range(len(prices)):
            if cur > prices[r]:
                cur = prices[r]
                l = r
            res = max(res, prices[r]-cur)
        return res
