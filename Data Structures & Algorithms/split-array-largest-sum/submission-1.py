class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(s):
            currSum = 0
            subArray = 1
            for n in nums:
                currSum += n
                if currSum > s:
                    subArray += 1
                    if subArray > k:
                        return False
                    currSum = n
            return True
                
        

        l,r = max(nums), sum(nums)
        res = 0
        while l<=r:
            m = (l+r) >> 1
            if canSplit(m):
                res = m
                r = m-1
            else:
                l = m+1
        return res