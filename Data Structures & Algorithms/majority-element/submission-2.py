class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        c = 0

        for n in nums:
            if n == major:
                c += 1
            else:
                c -= 1
                if c == 0:
                    major = n
                    c += 1
        return major
        