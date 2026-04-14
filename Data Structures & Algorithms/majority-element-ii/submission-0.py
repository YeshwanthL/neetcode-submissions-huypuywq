class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numMap = {}

        for num in nums:
            numMap[num] = numMap.get(num, 0) + 1
            if len(numMap) <= 2:
                continue
            
            new_count = {}
            for n,c in numMap.items():
                if c>1:
                    new_count[n] = c-1
            numMap = new_count
        
        res = []
        for num in numMap:
            if nums.count(num) > (len(nums)//3):
                res.append(num)

        return res
        