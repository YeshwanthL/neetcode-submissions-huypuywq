class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1,x
        res = 0
        while l <= r:
            m = (l+r) >> 1
            if m*m == x:
                return m
            elif m*m > x:
                r = m-1
            else:
                l = m+1
                res = m
        return res