class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i,n in enumerate(nums):
            x = target-n
            if x in index:
                return [index[x], i]
            index[n] = i
        return [-1, -1]