class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minProfit = [(c,p) for c,p in zip(capital, profits)]
        heapq.heapify(minProfit)

        for _ in range(k):
            while minProfit and minProfit[0][0] <= w:
                c,p = heapq.heappop(minProfit)
                heapq.heappush(maxProfit, -p)
            
            if not maxProfit:
                break
            
            w += -heapq.heappop(maxProfit)
        
        return w