class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        for n in numSet:
            tmp = 1
            if n+1 in numSet:
                while n+1 in numSet:
                    tmp += 1
                    n += 1
            res = max(res,tmp)
        return res