class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l * 2

        for i,n in enumerate(nums):
            res[i] = res[i+l] = n
        
        return res