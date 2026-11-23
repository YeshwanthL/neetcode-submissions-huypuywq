class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        res = total
        l,r = 1, total

        while l <= r:
            rate = l+r >> 1
            tmp = 0
            for b in piles:
                tmp += math.ceil(float(b)/rate)
            if tmp <= h:
                res = rate
                r = rate-1
            else:
                l = rate+1
        return res
            
