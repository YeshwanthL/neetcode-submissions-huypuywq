class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * 2 * n

        for i,v in enumerate(nums):
            res[i], res[i+n] = nums[i], nums[i]
        return res