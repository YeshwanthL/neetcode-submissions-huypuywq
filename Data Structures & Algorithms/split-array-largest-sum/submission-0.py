class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(val):
            subArray = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > val:
                    subArray += 1
                    if subArray > k:
                        return False
                    curSum = n
            return True
        
        l,r = max(nums), sum(nums)
        res = float("infinity")
        while l <=r:
            m = (l+r) >> 1
            if canSplit(m):
                res = min(res, m)
                r = m-1
            else:
                l = m+1
        return res