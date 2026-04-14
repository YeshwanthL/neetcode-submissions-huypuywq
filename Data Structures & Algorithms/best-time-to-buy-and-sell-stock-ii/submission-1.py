class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        res = 0
        for i in range(len(prices)):
            if l >= prices[i]:
                l = prices[i]
            else:
                res += prices[i] - l
                l = prices[i]
        return res


        