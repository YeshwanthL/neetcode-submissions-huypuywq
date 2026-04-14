class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,n in enumerate(nums):
            l,r = i+1,len(nums)-1
            while l < r:
                curr = nums[l] + nums[r] + n
                if curr == 0:
                    if [n, nums[l], nums[r]] not in res:
                        res.append([n, nums[l], nums[r]])
                if curr > 0:
                    r -= 1
                else:
                    l += 1
        return res
        