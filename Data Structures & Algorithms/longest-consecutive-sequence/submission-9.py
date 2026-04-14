class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for n in numSet:
            l = 1
            while n+1 in numSet:
                n+=1
                l+=1
            res = max(res,l)
        
        return res