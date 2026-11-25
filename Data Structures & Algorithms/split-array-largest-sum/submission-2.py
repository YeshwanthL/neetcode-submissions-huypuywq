class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(val):
            subArr = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > val:
                    subArr +=1
                    if subArr > k:
                        return False
                    curSum = n
            return True

        l, r = max(nums), sum(nums)
        res = float("infinity")
        while l <= r:
            m = (l+r) >> 1
            if canSplit(m):
                res = min(res, m)
                r = m-1
            else:
                l=m+1
        return res