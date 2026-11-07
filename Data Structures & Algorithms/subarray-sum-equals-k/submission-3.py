class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = {0:1}
        cur = 0
        res = 0
        for n in nums:
            cur += n
            diff = cur-k
            if diff in pre:
                res += pre[diff]
            pre[cur] = 1 + pre.get(cur,0)
        return res