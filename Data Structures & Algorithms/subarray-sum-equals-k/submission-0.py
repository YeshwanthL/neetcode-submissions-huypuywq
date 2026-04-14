class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        pre = {0:1}
        res = 0
        for n in nums:
            curr += n
            diff = curr - k
            if diff in pre:
                res += pre[diff]
            pre[curr] = 1 + pre.get(curr,0)
        return res
