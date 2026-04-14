class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        size = n * 2
        res = [0] * size

        for i in range(n):
            res[i], res[i+n] = nums[i], nums[i]
        
        return res

        