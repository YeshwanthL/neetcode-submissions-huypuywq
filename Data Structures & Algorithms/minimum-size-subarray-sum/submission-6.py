class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("infinity")
        l,r = 0, 0
        cur = 0
        while r < len(nums):
            cur += nums[r]
            while cur >= target:
                res = min(res, r-l+1)
                cur -= nums[l]
                l += 1
            r += 1
        return 0 if res == float("infinity") else res         