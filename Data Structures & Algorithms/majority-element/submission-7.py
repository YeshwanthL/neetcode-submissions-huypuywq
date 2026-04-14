class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major=count=0

        for n in nums:
            if count == 0:
                major = n
            count += ( 1 if major == n else - 1)
        return major

        