class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        low = prices[l]
        profit=0
        r=l+1
        while r < len(prices):
            if prices[l] > prices[r]:
                low=prices[r]
                l=r
                r+=1
            else:
                profit = max(profit,prices[r] - low)
                r+=1
        return profit
