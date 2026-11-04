class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for n in num_set:
            if n-1 not in num_set:
                tmp = 1
                while n+tmp in num_set:
                    tmp += 1
                res = max(res, tmp)
        return res