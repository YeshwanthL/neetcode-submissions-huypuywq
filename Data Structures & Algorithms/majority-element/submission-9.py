class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev, c = 0, 0
        for n in nums:
            if c == 0:
                prev = n
                c += 1
            elif n != prev:
                c -= 1
            else:
                c += 1
        return prev

