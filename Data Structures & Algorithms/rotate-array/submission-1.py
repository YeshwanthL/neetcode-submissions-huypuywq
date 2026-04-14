class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        l = 0
        r = len(nums)-1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l,r = 0,k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l=k
        r=len(nums)-1

        while l<r:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums