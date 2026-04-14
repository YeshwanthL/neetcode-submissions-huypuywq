class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l= 0
        res = float("inf")
        sub = 0
        for r in range(len(nums)):
            sub += nums[r]
            while sub >= target:
                res = min(res, r-l+1)
                sub -= nums[l]
                l += 1
        return 0 if res == float("inf") else res       