class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum (k, start, target):
            if k == 2:
                l,r = start, len(nums)-1

                while l<r:
                    curr = nums[l] + nums[r]
                    if curr == target:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l<r and nums[l] == nums[l-1]:
                            l += 1
                        while l<r and nums[r] == nums[r+1]:
                            r -= 1
                    elif curr > target:
                        r -= 1
                    else:
                        l += 1
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                quad.append(nums[i])
                kSum(k-1, i+1, target-nums[i])
                quad.pop()

        nums.sort()
        quad = []
        res = []
        kSum(4, 0, target)
        return res