class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = c = 0

        for n in nums:
            if c == 0:
                major = n
            c += ( 1 if n == major else -1)
        return major
        