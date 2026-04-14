class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        twosum = {}

        for i,n in enumerate(nums):
            sum = target - n
            if sum in twosum:
                return [twosum[sum],i]
            twosum[n]=i