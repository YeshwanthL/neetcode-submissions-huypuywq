class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i,n in enumerate(nums):
            two = target-n
            if two in Map:
                return [Map[two],i]
            Map[n]=i
        return []