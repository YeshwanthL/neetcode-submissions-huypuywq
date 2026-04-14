class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res=[]
        
        rDict = dict()

        for i,n in enumerate(nums):
            diff = target-n
            if diff in rDict:
                return [rDict[diff],i]
            rDict[n]=i
        
        return [-1,-1]
            
